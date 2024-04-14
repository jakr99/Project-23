from automata.fa.nfa import NFA

prob_1_19b = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1', 'q3'}, '1': {'q0'}, '': {'q6'}},  # Transition to q1 on 0, q3 on 0, or stay on q0 on epsilon
        'q1': {'0': {'q2'}},                                 # Transition to q2 on 0 (part of '00')
        'q2': {'1': {'q6'}},                                 # Transition to q6 on 1 (if '00' is followed by '11')
        'q3': {'1': {'q4'}},                                 # Transition to q4 on 1 (part of '01')
        'q4': {'': {'q6'}},                                  # Epsilon transition to q6
        'q5': {'1': {'q6'}},                                 # Transition to q6 on 1 (completing '11')
        'q6': {'': {'q0'}},                                  # Epsilon transition back to q0 to repeat the sequence
    },
    initial_state='q0',
    final_states={'q0', 'q6'}  # q0 is accepting because the sequence can be empty; q6 because it completes any valid sequence
)