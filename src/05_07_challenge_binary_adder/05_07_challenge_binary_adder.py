from qiskit import *
from qiskit_aer import *
from qiskit.visualization import plot_bloch_multivector
#%matplotlib inline

circuit = QuantumCircuit(4, 2)
circuit.x(0) # initalize input A
circuit.x(1) # initalize input B
circuit.barrier()

### YOUR CODE GOES HERE ###

# sum (q2)
circuit.cx(0, 2)
circuit.cx(1, 2)

# carryout (q3)
circuit.cswap(0, 1, 3)
# could also use:
#circuit.ccx(0, 1, 3)

circuit.barrier()
circuit.measure(2, 0) # measure SUM
circuit.measure(3, 1) # measure CARRY-OUT
circuit.draw(output='mpl')
circuit.draw()
# output:
#      ┌───┐ ░               ░
# q_0: ┤ X ├─░───■────────■──░───────
#      ├───┤ ░   │        │  ░
# q_1: ┤ X ├─░───┼────■───X──░───────
#      └───┘ ░ ┌─┴─┐┌─┴─┐ │  ░ ┌─┐
# q_2: ──────░─┤ X ├┤ X ├─┼──░─┤M├───
#            ░ └───┘└───┘ │  ░ └╥┘┌─┐
# q_3: ──────░────────────X──░──╫─┤M├
#            ░               ░  ║ └╥┘
# c: 2/═════════════════════════╩══╩═
#                               0  1

plot_bloch_multivector(StatevectorSimulator().run(circuit).result().get_statevector())

# simulate circuit and print message with SUM and CARRY-OUT states
simulator = QasmSimulator()
result = simulator.run(circuit, shots=1).result()
counts = result.get_counts()
print(f'SUM is {list(counts.keys())[0][1]}')
# SUM is 0
print(f'CARRY-OUT is {list(counts.keys())[0][0]}')
# CARRY-OUT is 1

# classical 2-bit adder gate:

# A ---.--))-----\
#      |   )) XOR >--. Sum
# B -.-|--))-----/
#    | |
#    | +--|----)
#    |    | AND )--. Carry-Out
#    +----|----)

# 1 + 1 = 2
# input     output
#  A B   Sum Carry-Out
#  0 0    0      0
#  0 1    1      0
#  1 0    1      0
#  1 1    1      1

# for this exercise, we want:
#   input     output
#   A   B     Sum Carry-Out
#  |0> |0>    |0>    |0>
#  |0> |1>    |1>    |0>
#  |1> |0>    |1>    |0>
#  |1> |1>    |1>    |1>

# CNOT|00> = |00>
# CNOT|01> = |01>
# CNOT|10> = |11>
# CNOT|11> = |10>

# CCNOT|000> = |000>
# CCNOT|001> = |001>
# CCNOT|010> = |010>
# CCNOT|011> = |011>
# CCNOT|100> = |100>
# CCNOT|101> = |101>
# CCNOT|110> = |111>
# CCNOT|111> = |110>

# SWAP|00> = |00>
# SWAP|01> = |10>
# SWAP|10> = |01>
# SWAP|11> = |11>

# CSWAP|000> = |000>
# CSWAP|001> = |001>
# CSWAP|010> = |010>
# CSWAP|011> = |011>
# CSWAP|100> = |100>
# CSWAP|101> = |110>
# CSWAP|110> = |101>
# CSWAP|111> = |111>
