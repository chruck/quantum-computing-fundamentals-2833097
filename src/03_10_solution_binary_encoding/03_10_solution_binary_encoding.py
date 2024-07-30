from qiskit import *
from qiskit.visualization import plot_state_qsphere
import qiskit_aer
#from math import pi
%matplotlib inline

# initialize a quantum circuit with 4 qubits
circuit = QuantumCircuit(4)

# set the qubits into the basis state |1101> using Pauli logic gates
circuit.x(0)
circuit.z(1)
circuit.y(2)
circuit.y(3)

# answer given
#circuit.x([0, 2, 3])

circuit.draw(output='mpl')

#simulator = Aer.get_backend('statevector_simulator')
simulator = qiskit_aer.StatevectorSimulator()
#result = execute(circuit, backend=simulator).result()
result = simulator.run(circuit).result()
statevector = result.get_statevector()
plot_state_qsphere(statevector)
