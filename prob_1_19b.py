from automata.fa.nfa import NFA

prob_1_19b = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0', 'q1'}, '1': {'q2'}, '': {'q7'}},
        'q1': {'0': {'q0'}, '1': {'q3'}},
        'q2': {'1': {'q4'}},
        'q3': {'0': {'q5'}},
        'q4': {'0': {'q6'}},
        'q5': {'1': {'q7'}},
        'q6': {'0': {'q7'}, '1': {'q2'}},
        'q7': {'0': {'q7'}, '': {'q0'}}
    },
    initial_state='q0',
    final_states={'q0', 'q7'}
)