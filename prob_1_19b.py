from automata.fa.nfa import NFA

prob_1_19b = NFA(
    states={'q_start', 'q0', 'q00', 'q00_1', 'q0011', 'q01', 'q_accept'},
    input_symbols={'0', '1'},
    transitions={
        'q_start': {'': {'q0', 'q_accept'}},  # Start state, can go to q0 or accept on epsilon
        'q0': {'0': {'q00', 'q01'}, '1': {'q_accept'}},  # Transition to handle "0" or "01"
        'q00': {'1': {'q00_1'}, '0': {'q00'}},  # Stay on q00 on "0", move to q00_1 on "1"
        'q00_1': {'1': {'q0011'}},  # Transition for "00" followed by "11"
        'q0011': {'': {'q_accept'}},  # Transition back to accept on epsilon
        'q01': {'': {'q_accept'}},  # Transition back to accept on epsilon for "01"
        'q_accept': {'': {'q0'}}  # Transition on epsilon back to q0 to allow repetition
    },
    initial_state='q_start',
    final_states={'q_accept'}  # Accepting state
)