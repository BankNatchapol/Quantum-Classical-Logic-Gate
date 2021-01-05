import classical
import quantum
from TOKEN import ACCESS_TOKEN
import pandas as pd
from tabulate import tabulate

sbits = [0, 1]
tbits = [(0, 0), (0, 1), (1, 0), (1, 1)]

table = pd.DataFrame(columns=['bit', 'not'])
for bit in sbits:
    table = table.append({'bit': bit, 'not': classical.not_gate(bit)}, ignore_index=True)
print(table,end="\n")

gates = [('and', classical.and_gate, quantum.and_gate),
         ('or', classical.or_gate, quantum.or_gate),
         ('xor', classical.xor_gate, quantum.xor_gate)]

for i in range(len(gates)):
    classicalTable = pd.DataFrame(columns=['bit1', 'bit2', gates[i][0]])
    quantumTable = pd.DataFrame(columns=['bit1', 'bit2', gates[i][0]])
    for bit in tbits:
        classicalTable = classicalTable.append({'bit1': bit[0], 'bit2': bit[1], gates[i][0]: gates[i][1](bit[0], bit[1])}, ignore_index=True)
        quantumTable = quantumTable.append({'bit1': bit[0], 'bit2': bit[1], gates[i][0]: gates[i][2](bit[0], bit[1])}, ignore_index=True)

    print(tabulate(classicalTable, headers='keys', tablefmt='psql'))
    print(tabulate(quantumTable, headers='keys', tablefmt='psql'))
    print()

