"from qiskit import *\n"
"from qiskit.tools.visualization import plot_bloch_multivector, array_to_latex\n"
"from math import pi\n"
"%matplotlib inline"
"circuit = QuantumCircuit(1)\n"
"circuit.draw(output='mpl')"
"simulator = Aer.get_backend('statevector_simulator')\n"
"result = execute(circuit, backend=simulator).result()\n"
"statevector = result.get_statevector()\n"
"array_to_latex(statevector, prefix=\"\\\\text{statevector = }\\n\")"
"plot_bloch_multivector(statevector)"
"from qiskit import *\n"
"from qiskit.tools.visualization import plot_bloch_multivector, array_to_latex\n"
"from math import pi\n"
"%matplotlib inline"
"circuit = QuantumCircuit(2)\n"
"circuit.ry(pi/4, [0, 1])\n"
"circuit.y(1)\n"
"circuit.draw(output='mpl')"
"simulator = Aer.get_backend('statevector_simulator')\n"
"result = execute(circuit, backend=simulator).result()\n"
"statevector = result.get_statevector()\n"
"array_to_latex(statevector, prefix=\"\\\\text{statevector = }\\n\")"
"plot_bloch_multivector(statevector)"