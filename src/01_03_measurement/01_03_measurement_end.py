#from qiskit import *
import qiskit
#from qiskit.tools.visualization import plot_histogram
# visualization is no longer in tools
import qiskit.visualization

# Magic for Jupyter
#%matplotlib inline


# A quantum register with 1 qubit
#qr = QuantumRegister(1)
qr = qiskit.QuantumRegister(1)

# A classical register with 1 bit
#cr = ClassicalRegister(1)
cr = qiskit.ClassicalRegister(1)

# A quantum circuit with those 2 registers
#circuit = QuantumCircuit(qr, cr)
circuit = qiskit.QuantumCircuit(qr, cr)

# since initialized qubit is always measured as 0, adding the Hadamard
# quantum operation, aka H-gate
circuit.h(qr)
circuit.measure(qr, cr)

# Aer is no longer part of qiskit, now in its own library
import qiskit_aer

#simulator = Aer.get_backend('qasm_simulator')
#simulator = qiskit_aer.AerSimulator()
simulator = qiskit_aer.QasmSimulator()

# execute() replaced with run()
# default number of shots is 1024
#result = execute(circuit, backend=simulator, shots=1024000).result()
result = simulator.run(circuit, shots=1024000).result()
#plot_histogram(result.get_counts())
qiskit.visualization.plot_histogram(result.get_counts())
print(result.get_counts())
