from math import pi
from qiskit import *
from qiskit.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
import qiskit_aer
#%matplotlib inline

circuit = QuantumCircuit(1, 1)
circuit.x(0)  # apply Pauli-X gate to zeroth qubit
circuit.h(0)  # apply Hadamard gate to zeroth qubit
circuit.h(0)  # apply Hadamard gate to zeroth qubit
circuit.draw(output='mpl')

#simulator = Aer.get_backend('statevector_simulator')
simulator = qiskit_aer.StatevectorSimulator()
#result = execute(circuit, backend=simulator).result()
result = simulator.run(circuit).result()
statevector = result.get_statevector()
array_to_latex(statevector, prefix="\\text{statevector = }\n")
# note that 1/sqrt(2) = sqrt(2)/2

plot_bloch_multivector(statevector)

circuit.measure(0, 0)
circuit.draw(output='mpl')

#simulator = Aer.get_backend('qasm_simulator')
simulator = qiskit_aer.QasmSimulator()
#result = execute(circuit, backend=simulator, shots=1024).result()
result = simulator.run(circuit, shots=1024000).result()
plot_histogram(result.get_counts())
