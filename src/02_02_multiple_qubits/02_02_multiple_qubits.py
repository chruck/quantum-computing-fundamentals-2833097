from qiskit import QuantumCircuit, QuantumRegister
from qiskit.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
import qiskit_aer

#%matplotlib inline

# replace
#qr = QuantumRegister(2)
#cr = ClassicalRegister(2)
#circuit = QuantumCircuit(qr, cr)
# with:
circuit = QuantumCircuit(2)

circuit.h(0)  # apply Hattimer (HGate) on first qubit
#circuit.measure(qr,cr)
circuit.measure_all()

#simulator = Aer.get_backend('qasm_simulator')
#simulator = qiskit_aer.AerSimulator()
#simulator = qiskit_aer.StatevectorSimulator()
simulator = qiskit_aer.AerSimulator()
#result = execute(circuit, backend=simulator).result()
result = simulator.run(circuit, shots=1001).result()
counts = result.get_counts()
plot_histogram(counts)

qiskit.visualization.plot_histogram(result.get_counts())
