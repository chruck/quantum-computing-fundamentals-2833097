import qiskit
#from qiskit.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
import qiskit.visualization

# Magic for Jupyter
#%matplotlib inline

qr = qiskit.QuantumRegister(1)
cr = qiskit.ClassicalRegister(1)
circuit = qiskit.QuantumCircuit(qr, cr)
circuit.h(0)
# Once measured, superposition is collapsed:
#circuit.measure(qr, cr)

import qiskit_aer

#simulator = qiskit_aer.AerSimulator()
#simulator = qiskit_aer.QasmSimulator()
simulator = qiskit_aer.StatevectorSimulator()

#result = simulator.run(circuit, shots=102400).result()
result = simulator.run(circuit).result()
#qiskit.visualization.plot_histogram(result.get_counts())
statevector = result.get_statevector()
#print(result.get_counts())
#print(statevector)
qiskit.visualization.array_to_latex(statevector)

qiskit.visualization.plot_bloch_multivector(statevector)

# Notes:
# Named vectors:
# Z-axis:  |0> = [ 1 ]  and  |1> = [ 0 ]
#                [ 0 ]             [ 1 ]
# X-axis:  |+> = [ 1/sqrt(2) ]  and  |-> = [ 1/sqrt(2)  ]
#                [ 1/sqrt(2) ]             [ -1/sqrt(2) ]
# Y-axis:  |+i> = [ 1/sqrt(2) ]  and  |-i> = [ 1/sqrt(2)  ]
#                 [ i/sqrt(2) ]              [ -i/sqrt(2) ]
# (sometimes Qiskit represents 1/sqrt(2) as sqrt(2)/2)
