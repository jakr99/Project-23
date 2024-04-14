from automata.fa.nfa import NFA

prob_1_19b = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1', 'q5'}, '1': {'q0'}},  # Can start "00" or "01", or stay in q0 on "1"
        'q1': {'0': {'q2'}},  # Handling "00"
        'q2': {'1': {'q3'}},  # Transitioning after "00" to handle "11"
        'q3': {'1': {'q4'}, '0': {'q2'}},  # Completing "11", allows restarting "00"
        'q4': {'': {'q0'}},  # Return to q0
        'q5': {'1': {'q6'}},  # Handling "01"
        'q6': {'': {'q0'}}  # Return to q0
    },
    initial_state='q0',
    final_states={'q0'}
)