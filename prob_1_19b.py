from automata.fa.nfa import NFA

prob_1_19b = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1', 'q5'}, '': {'q0'}},  # From q0, start "00" or "01", or stay on q0 by ε-transition (Kleene star effect)
        'q1': {'0': {'q2'}},  # Handling "00"
        'q2': {'1': {'q3'}},  # Transition to start "11" after "00"
        'q3': {'1': {'q4'}},  # Complete "11"
        'q4': {'': {'q0'}},  # Return to q0 to allow repetition of the pattern
        'q5': {'1': {'q6'}},  # Handling "01"
        'q6': {'': {'q0'}},  # Return to q0 to allow repetition of the pattern
    },
    initial_state='q0',
    final_states={'q0'}
)