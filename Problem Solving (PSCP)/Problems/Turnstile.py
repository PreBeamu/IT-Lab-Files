"""Docstring"""

def main():
    """So this Turnstile is the thing
    that's blocking me from entering those gates!"""
    is_locked = True
    states_log = []
    crossed = 0

    while "END" not in states_log:
        state = input()
        states_log.append(state)

    for current_state in states_log:
        if is_locked:
            if current_state == "C":
                is_locked = False
        elif not is_locked:
            if current_state == "P":
                crossed += 1
                is_locked = True

    print(crossed)

main()
