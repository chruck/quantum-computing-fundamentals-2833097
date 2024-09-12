#!/bin/bash

# Convert Python programs with Qiskit v0 content to Qiskit v1 .

sed -i "s/Aer.get_backend('statevector_simulator')/StatevectorSimulator()/g" $1
sed -i "s/execute(\([^,]*\), backend=\(\s*\))/\2.run(\1)/g" $1
sed -i "s/qiskit.tools.visualization/qiskit.visualization/g" $1
echo 'from qiskit_aer import *' >>$1
sed -i "s/Aer.get_backend('qasm_simulator')/QasmSimulator()/g" $1
sed -i "s/execute(\([^,]*\), backend=\([^,]*\), shots=\([^)]*\))/\2.run(\1, shots=\3)/g" $1
