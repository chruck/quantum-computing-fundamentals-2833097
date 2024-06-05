# Challenge Goals

# - Instantiate a quantum circuit with one qubit and one classical bit
# - Measure the qubit and store the result in the classical bit
# - Simulate 1,000-plus shots and plot the results on a histogram
# - Display the state vector and Bloch sphere representation

import qiskit
import qiskit.visualization
import qiskit_aer

# Magic for Jupyter:
#%matplotlib inline

# - Instantiate a quantum circuit with one qubit and one classical bit

qr = qiskit.QuantumRegister(1)
cr = qiskit.ClassicalRegister(1)
circuit = qiskit.QuantumCircuit(qr, cr)

# - Measure the qubit and store the result in the classical bit

circuit.measure(qr, cr)

# - Simulate 1,000-plus shots and plot the results on a histogram

simulator = qiskit_aer.AerSimulator()
result = simulator.run(circuit, shots=1001).result()
qiskit.visualization.plot_histogram(result.get_counts())

# - Display the state vector and Bloch sphere representation

simulator = qiskit_aer.StatevectorSimulator()
result = simulator.run(circuit).result()
statevector = result.get_statevector()
qiskit.visualization.array_to_latex(statevector)
qiskit.visualization.plot_bloch_multivector(statevector)
