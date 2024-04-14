from automata.fa.nfa import NFA

prob_1_19c = NFA(
    states={'q0'},
    input_symbols=set(),
    transitions={
        'q0': {'': {'q0'}}  # Only an epsilon transition to itself
    },
    initial_state='q0',
    final_states={'q0'}  # Accepting the empty string
)