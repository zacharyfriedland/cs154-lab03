# Our goal in this exercise is to implement a simplified 1-bit ALU
# that has 2 data inputs: {a, b}, 2 outputs: {r, cout},
# and compute one of the following 3 functions: r = a and b,
# r = a xnor b, and cout, r = a + b

import pyrtl

# Declare two 1-bit data inputs: a, b
a = pyrtl.Input(bitwidth=1, name='a')
b = pyrtl.Input(bitwidth=1, name='b')

# Declare two 1-bit outputs: r, cout
r = pyrtl.Output(bitwidth=1, name='r')
cout = pyrtl.Output(bitwidth=1, name='cout') 

# Declare control inputs
op = pyrtl.Input(bitwidth=2, name='op')

def half_adder(a, b):
    """
        ha_carry_out, ha_sum = a + b
    """
    ha_sum = # < add your code here >
    ha_carry_out = # < add your code here >
    return ha_sum, ha_carry_out


def alu (a, b, op):
    """
        Implementation of the desired simplified ALU:
        if op == 0: return a and b
        else if op == 1: return a xnor b
        else if op == 2" return a + b
    """
    # Operation 0: a and b
    op0 = # < add your code here >
    # Operation 1: a xnor b
    op1 = # < add your code here >
    # Operation 2: a + b
    op2_s, op2_c = half_adder(a, b)
    # Based on the given "op", return the proper signals as outputs
    alu_r = pyrtl.WireVector(bitwidth=1)
    alu_cout = pyrtl.WireVector(bitwidth=1)
    # < add your code here >
    return alu_r, alu_cout

# Call the above-defined "alu" function and connect its results to the block's output ports 
temp_r, temp_cout = alu(a, b, op)
r <<= temp_r
cout <<= temp_cout

# Testbench
simvals = {
    'a':    "010101010101",
    'b':    "001100110011",
    'op':   "000011112222"
}

# Simulate and test your "alu" design
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(12):
    sim.step({
        'a' : int(simvals['a'][cycle]),
        'b' : int(simvals['b'][cycle]),
        'op': int(simvals['op'][cycle])
        }) 
sim_trace.render_trace()

# Verification of the simulated design -- cross comparison with a software model
for cycle in range(12):
    if sim_trace.trace['op'][cycle] == 0:
        python_r = sim_trace.trace['a'][cycle] & sim_trace.trace['b'][cycle]
    elif sim_trace.trace['op'][cycle] == 1:
        not_int = lambda x: 0 if( x == 1) else 1
        python_r = not_int(sim_trace.trace['a'][cycle] ^ sim_trace.trace['b'][cycle])
    elif sim_trace.trace['op'][cycle] == 2:
        python_r = int("{0:02b}".format(sim_trace.trace['a'][cycle] + sim_trace.trace['b'][cycle])[1])
    python_cout = int("{0:02b}".format(sim_trace.trace['a'][cycle] + sim_trace.trace['b'][cycle])[0])
    if (python_r != sim_trace.trace['r'][cycle] or (python_cout != sim_trace.trace['cout'][cycle] and sim_trace.trace['op'][cycle] == 2)):
        print('The design is broken! Time for debugging.')
        exit(1)

print('The design passed the test! Congrats!')
