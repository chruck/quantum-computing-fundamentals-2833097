import qiskit
import qiskit.visualization

#%matplotlib inline

qr = qiskit.QuantumRegister(1)
cr = qiskit.ClassicalRegister(1)
circuit = qiskit.QuantumCircuit(qr, cr)
circuit.h(0)
circuit.measure(qr, cr)

import qiskit_aer

simulator = qiskit_aer.AerSimulator()

result = simulator.run(circuit, shots=102400).result()
qiskit.visualization.plot_histogram(result.get_counts())
print(result.get_counts())
