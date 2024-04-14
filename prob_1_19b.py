from automata.fa.nfa import NFA

prob_1_19b = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1', 'q5'}, '': {'q0'}},
        'q1': {'0': {'q2', 'q3'}},
        'q2': {'1': {'q0'}},  # This accounts for the (00)* part
        'q3': {'1': {'q4'}},  # This is the start of the (11) part
        'q4': {'': {'q0'}},   # This transition completes the (00)*(11) and loops back for repetition
        'q5': {'1': {'q0'}}   # This accounts for the 01 part
    },
    initial_state='q0',
    final_states={'q0'}
)