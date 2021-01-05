import classical
import quantum
from TOKEN import ACCESS_TOKEN
import pandas as pd
sbits = [0, 1]
tbits = [(0, 0), (0, 1), (1, 0), (1, 1)]

table = pd.DataFrame(columns=['bit', 'not'])
for bit in sbits:
    table = table.append({'bit': bit, 'not': classical.not_gate(bit)}, ignore_index=True)
print(table)
# print()
# print(f"Classical NOT : {bit1}->{classical.not_gate(bit1)}")
# print(f"Quantum   NOT : {bit1}->{quantum.not_gate(bit1)}\n")
# print(f"Classical AND : ({bit1}, {bit2})->{classical.and_gate(bit1, bit2)}")
# print(f"Quantum   AND : ({bit1}, {bit2})->{quantum.and_gate(bit1, bit2)}\n")
# print(f"Classical OR  : ({bit1}, {bit2})->{classical.or_gate(bit1, bit2)}")
# print(f"Quantum   OR  : ({bit1}, {bit2})->{quantum.or_gate(bit1, bit2)}\n")
# print(f"Classical XOR : ({bit1}, {bit2})->{classical.xor_gate(bit1, bit2)}")
# print(f"Quantum   XOR : ({bit1}, {bit2})->{quantum.xor_gate(bit1, bit2)}")
