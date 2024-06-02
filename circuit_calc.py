import math
import os
from warnings import resetwarnings
os.system('clear')

#V = IR
voltage = 5 #5V
max_current_mA = 20 #mA
current = max_current_mA / 1000
resistance = int(voltage / current)

# print(f'The resistor should be {resistance} Ω\n')

class ParallelCircuit():
    resistors = []
    def __init__(self, resistance):
        self.resistance = resistance
        ParallelCircuit.resistors.append(self.resistance)

    def equivalentResistance():
        req = 0
        for resistor in ParallelCircuit.resistors:
            req += 1/resistor
        req = 1/req
        return req


first,second,third = ParallelCircuit(80), ParallelCircuit(50), ParallelCircuit(70)

req = ParallelCircuit.equivalentResistance()

print(f'The equivalent resistance is {req:.3f} Ω\n')