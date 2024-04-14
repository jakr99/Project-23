from automata.fa.nfa import NFA

prob_1_19a = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},  # Loop for any number of 0's and 1's, transition to q1 on 0
        'q1': {'0': {'q2'}},                     # Transition to q2 on 0
        'q2': {'0': {'q3'}},                     # Transition to q3 on 0
        'q3': {'0': {'q0'}, '1': {'q0'}},        # Transition back to q0 on any input, completing the sequence
    },
    initial_state='q0',
    final_states={'q3'}
)

