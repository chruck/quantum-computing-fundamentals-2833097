from qiskit import *
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import *
from math import pi
#%matplotlib inline

circuit = QuantumCircuit(3)
circuit.x(0)
circuit.h(1)
circuit.rx(-pi/4, 2)
#circuit.swap(1, 2)
circuit.cswap(0, 1, 2)
circuit.draw(output='mpl')

simulator = StatevectorSimulator()
result = simulator.run(circuit).result()
plot_bloch_multivector(result.get_statevector())

# Notes:

# SWAP and Fredkin (CSWAP) gates:

# SWAP gate "swaps" the quantum state of 2 qubits.
# diagram:

# q_0: ─X─
#       │
# q_1: ─X─

# matrix representation:

# SWAP = [ 1 0 0 0 ]
#        [ 0 0 1 0 ]
#        [ 0 1 0 0 ]
#        [ 0 0 0 1 ]

# Applying:

# SWAP|00> = [ 1 0 0 0 ][ 1 ] = [ 1 ] = |00> (unchanged)
#            [ 0 0 1 0 ][ 0 ]   [ 0 ]
#            [ 0 1 0 0 ][ 0 ]   [ 0 ]
#            [ 0 0 0 1 ][ 0 ]   [ 0 ]

# SWAP|11> = [ 1 0 0 0 ][ 0 ] = [ 0 ] = |11> (unchanged)
#            [ 0 0 1 0 ][ 0 ]   [ 0 ]
#            [ 0 1 0 0 ][ 0 ]   [ 0 ]
#            [ 0 0 0 1 ][ 1 ]   [ 1 ]

# SWAP|01> = [ 1 0 0 0 ][ 0 ] = [ 0 ] = |10>
#            [ 0 0 1 0 ][ 1 ]   [ 0 ]
#            [ 0 1 0 0 ][ 0 ]   [_1_]
#            [ 0 0 0 1 ][ 0 ]   [ 0 ]

# SWAP|10> = [ 1 0 0 0 ][ 0 ] = [ 0 ] = |01>
#            [ 0 0 1 0 ][ 0 ]   [_1_]
#            [ 0 1 0 0 ][ 1 ]   [ 0 ]
#            [ 0 0 0 1 ][ 0 ]   [ 0 ]

# Fredkin aka CSWAP (controlled-SWAP) does a swap of 2 qubits if a
# control qubit is |1> .
# diagram:

# q_0: ─■─  (control)
#       │
# q_1: ─X─
#       │
# q_2: ─X─

# matrix representation:

# CSWAP = [ 1 0 0 0 0 0 0 0 ]  notice this looks like:
#         [ 0 1 0 0 0 0 0 0 ]      [ I   0  ]
#         [ 0 0 1 0 0 0 0 0 ]      [ 0 SWAP ]
#         [ 0 0 0 1 0 0 0 0 ]
#         [ 0 0 0 0 1 0 0 0 ]
#         [ 0 0 0 0 0 0 1 0 ]
#         [ 0 0 0 0 0 1 0 0 ]
#         [ 0 0 0 0 0 0 0 1 ]
from qiskit_aer import *
from qiskit_aer import *
