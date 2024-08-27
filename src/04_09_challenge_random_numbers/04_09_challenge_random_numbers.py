from math import pi
from qiskit import *
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit_aer import QasmSimulator, StatevectorSimulator
#%matplotlib inline

circuit = QuantumCircuit(3)

##### YOUR CODE GOES HERE #####
# Goal:
# |001>  37.5%
# |011>  37.5%
# |101>  12.5%
# |111>  12.5%

circuit.y(0)  # or X gate
circuit.h(1)
circuit.rx(pi/3, 2)  # or Ry gate

simulator = StatevectorSimulator()
result = simulator.run(circuit).result()
plot_bloch_multivector(result.get_statevector())

circuit.measure_all()
circuit.draw(output='mpl')

simulator = QasmSimulator()
result = simulator.run(circuit, shots=1024000).result()
plot_histogram(result.get_counts())

# Notes:
# For 2 qubit system:
# |00> = [ 1 ]
#        [ 0 ]
#        [ 0 ]
#        [ 0 ]
# remember Pauli-X is:  X = [ 0 1 ]  (ie, a 2x2 matrix)
#                           [ 1 0 ]
# We can't simply matrix-multiply a 2x2 with a 4x1 matrix ( X|00> ).
# Also, no indication of which qubit that the Pauli-X is being applied
# to.
#
# Kronecker Product:
# - operation on 2 matrices that produces a block matrix
# - generalization of the _outer_product_ operation on 2 vectors
#   --> works on matrices
# - denoted by symbol: (x)  <-- circle with an 'x' inside
#   (same as outer product)
# eg:
# [ a b ] (x) [ w x ] = [ a[ w x ]  b[ w x ] ] = [ aw ax bw bx ]
# [ c d ]     [ y z ]   [  [ y z ]   [ y z ] ]   [ ay az by bz ]
#                       [ c[ w x ]  d[ w x ] ]   [ cw cx dw dx ]
#                       [  [ y z ]   [ y z ] ]   [ cy cz dy dz ]
# eg:
# q0 -------
# q1 --[X]--
#
# but need 2 matrices for 4x4, so add identity matrix (placeholder,
# doesn't affect state):
#
# q0 --[I]--
# q1 --[X]--
#
# since want X on second qubit, put X on left and I on right:
# X (x) I = [ 0 1 ] (x) [ 1 0 ] = [ 0 0 1 0 ] = [ _0 _I ] (simplified)
#           [ 1 0 ]     [ 0 1 ]   [ 0 0 0 1 ]   [ _I _0 ]
#                                 [ 1 0 0 0 ]
#                                 [ 0 1 0 0 ]
# where _0 is a 2x2 matrix of all zeros and _I is a 2x2 identity
# matrix
# To apply to both qubits from above:
# (X(x)I)|00> = [ 0 0 1 0 ][ 1 ] = [ 0 ] = |10>
#               [ 0 0 0 1 ][ 0 ]   [ 0 ]
#               [ 1 0 0 0 ][ 0 ]   [ 1 ]
#               [ 0 1 0 0 ][ 0 ]   [ 0 ]
#
# In 2-qubit operation (X(x)Y)|AB> , X gate is applied to qubit A and
# Y is applied to B.
