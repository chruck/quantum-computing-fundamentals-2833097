# Pauli-Z gate
# - single-qubit rotation of pi radians around Z axis on Bloch sphere
# - represented as:
#   - Z
#   - (sigma sub Z)?
#   - [ 1  0 ]
#     [ 0 -1 ]
# - therefore, eg, Z|0> = |0>  and  Z|1> = -|1>  because
#   [ 1  0 ][ 1 ] = [ 1 ]  and  [ 1  0 ][ 0 ] = [  0 ] = -[ 0 ]
#   [ 0 -1 ][ 0 ]   [ 0 ]       [ 0 -1 ][ 1 ]   [ -1 ]    [ 1 ]
#   ultimately,  Z|psi> = [ 1  0 ][ alpha ] = [ alpha ] = alpha|0>
#                         [ 0 -1 ][ beta  ]   [ -beta ]   - beta|1>

from qiskit import *
from qiskit.visualization import plot_bloch_multivector, array_to_latex
from math import pi
%matplotlib inline

circuit = QuantumCircuit(2)
circuit.ry(pi/4, [0, 1])
circuit.z(1)
circuit.draw(output='mpl')

import qiskit_aer
#simulator = Aer.get_backend('statevector_simulator')
simulator = qiskit_aer.StatevectorSimulator()
#result = execute(circuit, backend=simulator).result()
result = simulator.run(circuit).result()
statevector = result.get_statevector()
array_to_latex(statevector, prefix="\\text{statevector = }\n")
plot_bloch_multivector(statevector)
