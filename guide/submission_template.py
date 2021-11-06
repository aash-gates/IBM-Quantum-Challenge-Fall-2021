"""
Challenge 4c solver function for the IBM Quantum Fall Challenge 2021
Author: Firstname Lastname <xxxxx@email.com> # TODO 1: change to your name and email
Score: 312345 # TODO 1: change to your score

TODO:
1. Add author name, email and score at the top of the file
2. Write a summary of your approach in the header and highlight
the techniques that gave you the biggest improvement
3. Import all required libraries and modules
4. Print author name and score inside the `solver_function`
5. Copy code to each sub-functions (e.g.phase_return, subroutine_add_constant)
and explain the implementation in comments

# TODO 2: write summary of your approach
# TODO 2: please highlight the techniques that gave you the biggest improvement
Summary of the approach:
1.
2.
3.

"""
# TODO 3: import all required libraries and modules
from qiskit import QuantumCircuit, QuantumRegister


def solver_function(L1: list, L2: list, C1: list, C2: list, C_max: int) -> QuantumCircuit:
    # TODO 4: add your name and score here
    # print name and score
    author = 'Firstname Lastname'
    score = 312345
    print(f'{author}: {score}')

    # the number of qubits representing answers
    index_qubits = len(L1)

    # the maximum possible total cost
    max_c = sum([max(l0, l1) for l0, l1 in zip(C1, C2)])

    # the number of qubits representing data values can be defined using the maximum possible total cost as follows:
    data_qubits = math.ceil(math.log(max_c, 2)) + 1 if not max_c & (max_c - 1) == 0 else math.ceil(
        math.log(max_c, 2)) + 2

    ### Phase Operator ###
    # return part
    def phase_return():

    ##############################
    ### TODO ###
    ### Paste your code from above cells here ###
    # TODO 5: explain the implementation in comments

    ##############################

    # penalty part
    def subroutine_add_const():

    ##############################
    ### TODO ###
    ### Paste your code from above cells here ###

    ##############################

    # penalty part
    def const_adder():

    ##############################
    ### TODO ###
    ### Paste your code from above cells here ###

    ##############################

    # penalty part
    def cost_calculation():

    ##############################
    ### TODO ###
    ### Paste your code from above cells here ###

    ##############################

    # penalty part
    def constraint_testing():

    ##############################
    ### TODO ###
    ### Paste your code from above cells here ###

    ##############################

    # penalty part
