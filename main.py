import classical
import quantum
from TOKEN import ACCESS_TOKEN

bit1 = 0
bit2 = 1

print()
print(f"Classical NOT : {bit1}->{classical.not_gate(bit1)}")
print(f"Quantum   NOT : {bit1}->{quantum.not_gate(bit1, backend='real', token=ACCESS_TOKEN)}\n")
print(f"Classical AND : ({bit1}, {bit2})->{classical.and_gate(bit1, bit2)}")
print(f"Quantum   AND : ({bit1}, {bit2})->{quantum.and_gate(bit1, bit2, backend='real', token=ACCESS_TOKEN)}\n")
print(f"Classical OR  : ({bit1}, {bit2})->{classical.or_gate(bit1, bit2)}")
print(f"Quantum   OR  : ({bit1}, {bit2})->{quantum.or_gate(bit1, bit2, backend='real', token=ACCESS_TOKEN)}\n")
print(f"Classical XOR : ({bit1}, {bit2})->{classical.xor_gate(bit1, bit2)}")
print(f"Quantum   XOR : ({bit1}, {bit2})->{quantum.xor_gate(bit1, bit2, backend='real', token=ACCESS_TOKEN)}")
