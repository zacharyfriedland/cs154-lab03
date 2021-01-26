# fibonacci

import pyrtl

# Declare two 32-bit data inputs: A, B
A = pyrtl.Input(bitwidth=32, name='A')
B = pyrtl.Input(bitwidth=32, name='B')
reg_A = pyrtl.Register(bitwidth=32, name='reg_A')
reg_B = pyrtl.Register(bitwidth=32, name='reg_B')
reg_temp = pyrtl.Register(bitwidth=32, name='reg_temp')
reg_counter = pyrtl.Register(bitwidth=32, name='reg_counter')

# Declare one 32-bit outputs: result
result = pyrtl.Output(bitwidth=32, name='result')





with pyrtl.conditional_assignment:
    with reg_counter == 0:
        result |= A
        reg_A.next |= A
        reg_B.next |= B
        reg_temp.next |= A + B
        reg_counter.next |= reg_counter + 1
    with reg_counter == 1:
        result |= B
        reg_A.next |= reg_B
        reg_B.next |= reg_temp
        reg_temp.next |= reg_A + reg_B
        reg_counter.next |= reg_counter + 1
    with pyrtl.otherwise:
        reg_A.next |= reg_B
        reg_B.next |= reg_A + reg_B
        result |= reg_temp
        reg_temp.next |= reg_A + reg_B
        reg_counter.next |= reg_counter + 1

# Testbench
simvals = {
    'A':    "11111",
    'B':    "22222"
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
