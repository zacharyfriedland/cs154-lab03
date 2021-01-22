### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# As any Boolen circuit, a MUX can be implemented only with the use of AND, OR, 
# and NOT gates. Your first task is to Build a 1-bit 2:1 MUX out of these gates
# and then simulate it for 8 cycles using random inputs as above.

# Declare two 1-bit data inputs: a, b
a = pyrtl.Input(bitwidth=1, name='a')
b = pyrtl.Input(bitwidth=1, name='b')

# Declare one 1-bit control input: s
s = pyrtl.Input(bitwidth=1, name='s')

# Declare one 1-bit output: o_wg
o_wg = pyrtl.Output(bitwidth=1, name='o_wg')

# 2:1 MUX implementation using only AND, OR, and NOT gates
and1_res = pyrtl.WireVector(bitwidth=1, name='A & ~S')
and2_res = pyrtl.WireVector(bitwidth=1, name='B & S')


and1_res <<= a & (~s)
and2_res <<= b & s
o_wg <<= and1_res | and2_res


# Simulate and test the design for 8 clock cycles using random inputs
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

import random
for cycle in range(8):
    # Call "sim.step" to simulate each clock cycle of the design
    sim.step({
        'a': random.choice([0, 1]),
        'b': random.choice([0, 1]),
        's': random.choice([0, 1])
        })

# Print the trace results to the screen.
print('--- 1-bit 2:1 MUX Simulation -- Built using only AND, OR, and NOT gates ---')
sim_trace.render_trace()
