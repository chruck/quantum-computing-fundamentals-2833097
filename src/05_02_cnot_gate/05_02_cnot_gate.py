from qiskit import *
#from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import StatevectorSimulator
#%matplotlib inline
circuit = QuantumCircuit(3)
circuit.x(0)
circuit.cx(0, 1)
circuit.cx(1, 2)

circuit.draw(output='mpl')

#simulator = Aer.get_backend('statevector_simulator')
simulator = StatevectorSimulator()
#result = execute(circuit, backend=simulator).result()
result = simulator.run(circuit).result()
plot_bloch_multivector(result.get_statevector())

# Notes:
# Controlled-NOT Gate aka CNOT or CX
# - for 2 qubits, flips the _target_ qubit if the _control_ qubit is |1>
# - abbreviated as CNOT or CX (Controlled-X Gate)
# - diagram symbols:
#  q0 ---*---  ('*' is a solid dot)  <-- control qubit
#        |
#  q1 --(+)--  ('(+)' is a solid circle with a plus inside)  <-- target
# - control qubit is unchanged after CNOT gate operation applied
# CNOT = [ 1 0 0 0 ]
#        [ 0 1 0 0 ]
#        [ 0 0 0 1 ]
#        [ 0 0 1 0 ]
#   note the 2x2 identity matrix in top left corner, and bottom right
#   is Pauli-X:  [ I 0 ]
#                [ 0 X ]
#
# CNOT|00> = [ 1 0 0 0 ] [ 1 ] = [ 1 ] = |00>  (control is left 0)
#            [ 0 1 0 0 ] [ 0 ]   [ 0 ]
#            [ 0 0 0 1 ] [ 0 ]   [ 0 ]
#            [ 0 0 1 0 ] [ 0 ]   [ 0 ]
# CNOT|01> = [ 1 0 0 0 ] [ 0 ] = [ 0 ] = |01>
#            [ 0 1 0 0 ] [ 1 ]   [ 1 ]
#            [ 0 0 0 1 ] [ 0 ]   [ 0 ]
#            [ 0 0 1 0 ] [ 0 ]   [ 0 ]
# CNOT|10> = [ 1 0 0 0 ] [ 0 ] = [ 0 ] = |11>  (target, right, is flipped)
#            [ 0 1 0 0 ] [ 0 ]   [ 0 ]
#            [ 0 0 0 1 ] [ 1 ]   [ 0 ]
#            [ 0 0 1 0 ] [ 0 ]   [ 1 ]
# CNOT|11> = [ 1 0 0 0 ] [ 0 ] = [ 0 ] = |10>
#            [ 0 1 0 0 ] [ 0 ]   [ 0 ]
#            [ 0 0 0 1 ] [ 0 ]   [ 1 ]
#            [ 0 0 1 0 ] [ 1 ]   [ 0 ]
# - order of putting CX is important, and which is control and target
