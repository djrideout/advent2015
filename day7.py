from collections import defaultdict
import asyncio

async def eval_gate(str: str, wires):
    left, out = str.split(" -> ")
    inputs = left.split(" ")
    if len(inputs) == 1:
        if not wires[out].done():
            wires[out].set_result(int(inputs[0]) if inputs[0].isdigit() else await wires[inputs[0]])
    elif len(inputs) == 2:
        wires[out].set_result(~await wires[inputs[1]])
    else:
        a = int(inputs[0]) if inputs[0].isdigit() else await wires[inputs[0]]
        op = inputs[1]
        b = int(inputs[2]) if inputs[2].isdigit() else await wires[inputs[2]]
        match op:
            case "AND": wires[out].set_result(a & b)
            case "OR": wires[out].set_result(a | b)
            case "LSHIFT": wires[out].set_result(a << b)
            case "RSHIFT": wires[out].set_result(a >> b)

async def get_wire_a_value(input, defaults):
    wires = defaultdict(lambda: loop.create_future())
    for key in defaults:
        wires[key].set_result(defaults[key])
    evals = []
    for l in input:
        evals.append(eval_gate(l.rstrip(), wires))
    await asyncio.gather(*evals)
    return wires["a"].result()

async def main():
    input = open("input/day7.txt").readlines()
    a = await get_wire_a_value(input, {})
    print(a)
    print(await get_wire_a_value(input, { "b": a }))

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
