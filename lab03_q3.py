### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare data inputs
a = pyrtl.Input(bitwidth=3, name='a')
b = pyrtl.Input(bitwidth=3, name='b')
c = pyrtl.Input(bitwidth=3, name='c')
d = pyrtl.Input(bitwidth=3, name='d')
e = pyrtl.Input(bitwidth=3, name='e')


# Declare control inputs
s = pyrtl.Input(bitwidth=3, name='s')

# Declare outputs 
o = pyrtl.Output(bitwidth=3, name='o')

# Describe your 5:1 MUX implementation
with pyrtl.conditional_assignment:
    with s == 0b000:
        o |= a
    with s == 0b001:
        o |= b
    with s == 0b010:
        o |= c
    with s == 0b011:
        o |= d
    with pyrtl.otherwise:
        o |= e

# DO: Simulate and test your design for 16 clock cycles using random inputs
# Simulate and test your design for 8 clock cycles using random inputs
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

import random
for cycle in range(16):
    # Call "sim.step" to simulate each clock cycle of the design
    sim.step({
        'a': 0b000,
        'b': 0b001,
        'c': 0b010,
        'd': 0b011,
        'e': 0b100,
        's': random.choice([0b000, 0b001, 0b010, 0b011, 0b100])
    })

print('--- 3-bit 5:1 MUX Simulation -- Built using PyRTL conditionals ---')
sim_trace.render_trace()
