from automata.fa.nfa import NFA

# transitions for repeating 00 sequences
transitions_00_star = {
    'q1': {'0': {'q1'}, '': {'q3'}},  # loop on '0', move to 'q3' on epsilon to allow for `00*11`
    'q3': {'1': {'q4'}},  # transition to 'q4' on '1' to complete `11`
}

# transitions for the `01` part
transitions_01 = {
    'q5': {'1': {'q6'}},  # transition to 'q6' on '1' to complete `01`
}

# transitions to repeat the pattern (loop back to 'q0')
transitions_repeat = {
    'q4': {'': {'q0'}},  # epsilon transition back to 'q0' after `11`
    'q6': {'': {'q0'}}   # epsilon transition back to 'q0' after `01`
}

# Combine all transitions
transitions = {**transitions_00_star, **transitions_01, **transitions_repeat}

# Adding transitions from 'q0' to start `00*11` or `01`
transitions['q0'] = {'0': {'q1', 'q5'}, '1': {'q3'}}

prob_1_19b = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_symbols={'0', '1'},
    transitions=transitions,
    initial_state='q0',
    final_states={'q0', 'q4', 'q6'}
)