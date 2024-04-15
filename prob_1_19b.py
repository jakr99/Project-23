from automata.fa.nfa import NFA

prob_1_19b = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1', 'q5'}, '1': {'q3'}},
        'q1': {'0': {'q1'}, '1': {'q2'}},
        'q2': {'0': {'q0'}},
        'q3': {'1': {'q4'}},
        'q4': {'0': {'q0'}, '1': {'q0'}},
        'q5': {'1': {'q6'}},
        'q6': {'0': {'q0'}, '1': {'q0'}}
    },
    initial_state='q0',
    final_states={'q0', 'q4', 'q6'}
)