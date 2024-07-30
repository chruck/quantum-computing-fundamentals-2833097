# Pauli-Y gate
# - single-qubit rotation of pi radians around Y axis on Bloch sphere
# - represented as:
#   - Y
#   - (sigma sub Y)?
#   - [ 0 -i ]  or simplified "Alternative Pauli-Y":  [0 -1]
#     [ i  0 ]                                        [1  0]
# - therefore, eg, Y|0> = i|1>  and  Y|1> = -i|0>  because
#   [ 0 -i ][ 1 ] = [ 0 ] = i[ 0 ]  and  [ 0 -i ][ 0 ] = [ -i ] = -i[ 1 ]
#   [ i  0 ][ 0 ]   [ i ]    [ 1 ]       [ i  0 ][ 1 ]   [  0 ]     [ 0 ]
#   ultimately,  Y|psi> = [ 0 -i ][ alpha ] = i[ -beta ] = i( alpha|1>
#                         [ i  0 ][ beta  ]    [ alpha ]     - beta|0> )
#   Probability P(Y|0> = |0>) = |0|^2 = 0
#           and P(Y|0> = |1>) = |i|^2 = 1
#               P(Y|1> = |0>) = |-i|^2 = 1
#           and P(Y|1> = |1>) = |0|^2 = 0
#   |1> is physically indistinguishable from i|1>
# if |psi> = alpha|0> + beta|1> then
# Y|psi> = i( alpha|1> - beta|0> )

from qiskit import *
from qiskit.visualization import plot_bloch_multivector, array_to_latex
from math import pi
%matplotlib inline

#circuit = QuantumCircuit(1)
circuit = QuantumCircuit(2)
circuit.ry(pi/4, [0, 1])
circuit.y(1)
circuit.draw(output='mpl')

import qiskit_aer
#simulator = Aer.get_backend('statevector_simulator')
simulator = qiskit_aer.StatevectorSimulator()
#result = execute(circuit, backend=simulator).result()
result = simulator.run(circuit).result()
statevector = result.get_statevector()
array_to_latex(statevector, prefix="\\text{statevector = }\n")
plot_bloch_multivector(statevector)

