#Implement a basic finite state automaton that recognizes a specific language or pattern. In this example, we'll create a simple automaton to match strings ending with 'ab' using python.

def finite_automaton(string):
    state = "q0"
    for char in string:
        if state == "q0":
            if char == "a":
                state = "q1"
            else:
                state = "q0"
        elif state == "q1":
            if char == "a":
                state = "q1"
            elif char == "b":
                state = "q2"
            else:
                state = "q0"
        elif state == "q2":
            if char == "a":
                state = "q1"
            else:
                state = "q0"
    if state == "q2":
        return True
    else:
        return False
strings = ["ab", "aab", "abab", "abc", "aba", "bba"]
for string in strings:
    if finite_automaton(string):
        print(string, "-> Accepted")
    else:
        print(string, "-> Rejected")
