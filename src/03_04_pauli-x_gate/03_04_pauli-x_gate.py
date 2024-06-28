# Pauli-X gate
# - single-qubit rotation of pi radians around X axis on Bloch sphere
# - equivalent to classical NOT
# - represented as:
#   - X
#   - sigma sub X
#   - [ 0 1 ]
#     [ 1 0 ]
# - therefore, eg, X|0> = |1>  and  X|1> = |0>  because
#   [ 0 1 ][ 1 ] = [ 0 ]       and  [ 0 1 ][ 0 ] = [ 1 ]
#   [ 1 0 ][ 0 ]   [ 1 ]            [ 1 0 ][ 1 ]   [ 0 ]
#   ultimately,  X|psi> = [ 0 1 ][ alpha ] = [ beta  ]
#                         [ 1 0 ][ beta  ]   [ alpha ]

from qiskit import *
#from qiskit.tools.visualization import plot_bloch_multivector, array_to_latex
from qiskit.visualization import plot_bloch_multivector, array_to_latex
from math import pi

#%matplotlib inline

circuit = QuantumCircuit(1)
#circuit.ry(pi/4, 0)
circuit.ry(theta=pi/4, qubit=0)
circuit.x(0)  # add Pauli-X gate on [0]'th (only) qubit
circuit.x(0)  # second Pauli-X
print(circuit)  # prints:    ┌───┐
                #         q: ┤ X ├
                #            └───┘
circuit.draw()  #    ┌───┐
                # q: ┤ X ├
                #    └───┘
circuit.draw(output='mpl')  # output as img using matplotlib

import qiskit_aer
#simulator = Aer.get_backend('statevector_simulator')
simulator = qiskit_aer.StatevectorSimulator()
#result = execute(circuit, backend=simulator).result()
result = simulator.run(circuit).result()
statevector = result.get_statevector()
array_to_latex(statevector, prefix="\\\\text{statevector = }\\n")
plot_bloch_multivector(statevector)
