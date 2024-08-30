from qiskit import *
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import *
from math import pi
#%matplotlib inline

circuit = QuantumCircuit(3)
circuit.x(0)
circuit.x(1)
circuit.rx(pi/3, 2)
#circuit.ccx(0, 1, 2)  # note toffoli() is no longer in qiskit
circuit.draw(output='mpl')

simulator = StatevectorSimulator()
result = simulator.run(circuit).result()
plot_bloch_multivector(result.get_statevector())

circuit.ccx(0, 1, 2)
circuit.draw(output='mpl')
result = simulator.run(circuit).result()
plot_bloch_multivector(result.get_statevector())

# Notes:

# Controlled Controlled NOT Gate aka Toffoli Gate
# - uses 2 qubits as controls
# - target qubit is flipped if both control qubits are |1>
# - abbreviated as CCNOT or CCX (Control-Control-X-Gate)
# - represented as 8x8 matrix:
# CCNOT = [ 1 0 0 0 0 0 0 0 ]  note that top left 6x6 is Identity
#         [ 0 1 0 0 0 0 0 0 ]  matrix
#         [ 0 0 1 0 0 0 0 0 ]
#         [ 0 0 0 1 0 0 0 0 ]
#         [ 0 0 0 0 1 0 0 0 ]
#         [ 0 0 0 0 0 1 0 0 ]
#         [ 0 0 0 0 0 0 0 1 ]  and bottom right 2x2 is Pauli-X [ 0 1 ]
#         [ 0 0 0 0 0 0 1 0 ]                                  [ 1 0 ]
#
# only if both controls are |1> does target flip:
# CCNOT|110> = [ 1 0 0 0 0 0 0 0 ] [ 0 ] = [ 0 ] = |111>
#              [ 0 1 0 0 0 0 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 1 0 0 0 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 0 1 0 0 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 0 0 1 0 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 0 0 0 1 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 0 0 0 0 0 1 ] [ 1 ]   [ 0 ]
#              [ 0 0 0 0 0 0 1 0 ] [ 0 ]   [ 1 ]
# CCNOT|111> = [ 1 0 0 0 0 0 0 0 ] [ 0 ] = [ 0 ] = |110>
#              [ 0 1 0 0 0 0 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 1 0 0 0 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 0 1 0 0 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 0 0 1 0 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 0 0 0 1 0 0 ] [ 0 ]   [ 0 ]
#              [ 0 0 0 0 0 0 0 1 ] [ 0 ]   [ 1 ]
#              [ 0 0 0 0 0 0 1 0 ] [ 1 ]   [ 0 ]
# CCNOT|000> = |000>
# CCNOT|001> = |001>
# CCNOT|010> = |010>
# CCNOT|011> = |011>
# CCNOT|100> = |100>
# CCNOT|101> = |101>
# (and
# CCNOT|110> = |111>
# CCNOT|111> = |110>
# )
# - CCNOT is its own reverse:  applying twice gets target back to
# where it was.
# - rotated around X-axis
