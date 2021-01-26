# fibonacci

import pyrtl

# Declare two 32-bit data inputs: A, B
A = pyrtl.Input(bitwidth=32, name='A')
B = pyrtl.Input(bitwidth=32, name='B')
reg_A = pyrtl.Register(bitwidth=32, name='reg_A')
reg_B = pyrtl.Register(bitwidth=32, name='reg_B')
reg_temp = pyrtl.Register(bitwidth=32, name='reg_temp')

# Declare one 32-bit outputs: result
result = pyrtl.Output(bitwidth=32, name='result')


reg_temp.next <<= A + B
reg_A.next <<= reg_B
reg_B.next <<= reg_temp

with pyrtl.conditional_assignment:
    with reg_temp == 0:
        result |= A
        # with reg_A == 0:
        #     result |= B
        # with reg_B == 0:
        #     result |= A
    with pyrtl.otherwise:
        result |= reg_temp


# Testbench
simvals = {
    'A':    "00000",
    'B':    "11111"
}

# Simulate and test your "alu" design
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(5):
    sim.step({
        'A' : int(simvals['A'][cycle]),
        'B' : int(simvals['B'][cycle])
        }) 
sim_trace.render_trace()

# Verification of the simulated design -- cross comparison with a software model
# for cycle in range(12):
#     if sim_trace.trace['op'][cycle] == 0:
#         python_r = sim_trace.trace['a'][cycle] & sim_trace.trace['b'][cycle]
#     elif sim_trace.trace['op'][cycle] == 1:
#         not_int = lambda x: 0 if( x == 1) else 1
#         python_r = not_int(sim_trace.trace['a'][cycle] ^ sim_trace.trace['b'][cycle])
#     elif sim_trace.trace['op'][cycle] == 2:
#         python_r = int("{0:02b}".format(sim_trace.trace['a'][cycle] + sim_trace.trace['b'][cycle])[1])
#     python_cout = int("{0:02b}".format(sim_trace.trace['a'][cycle] + sim_trace.trace['b'][cycle])[0])
#     if (python_r != sim_trace.trace['r'][cycle] or (python_cout != sim_trace.trace['cout'][cycle] and sim_trace.trace['op'][cycle] == 2)):
#         print('The design is broken! Time for debugging.')
#         exit(1)

# print('The design passed the test! Congrats!')
