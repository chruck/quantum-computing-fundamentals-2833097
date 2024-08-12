from qiskit import *
#from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.visualization import plot_bloch_multivector
import qiskit_aer
#%matplotlib inline

circuit = QuantumCircuit(3)
circuit.h([0, 1, 2, 3, 4])
circuit.s(1)
circuit.sdg(2)
circuit.t(3)
circuit.tdg(4)
circuit.draw(output='mpl')

#simulator = Aer.get_backend('statevector_simulator')
simulator = qiskit_aer.StatevectorSimulator()
#result = execute(circuit, backend=simulator).result()
result = simulator.run(circuit).result()
plot_bloch_multivector(result.get_statevector())

# Notes:
# So far, been measuring |0> and |1>, which are along the Z-axis, (a
# "Z(-axis) measurement") but any 2 basis states could be measured,
# such as |+> and |-> (X-axis), |i> and |-i> (Y-axis), or any other
# orthogonal (opposite-pointing) pair (there are an infinite number).
#
# X-axis Measurement
# P(|psi> = |+>) = |<+|psi>|^2
# "The probability that (measuring) (quantum state, vector) ket Psi is
# ket Plus (state) is the absolute value of the inner product of bra
# Plus and ket Psi squared."
#
# P(|0> = |+>) = |<+|0>|^2 = |1/sqrt(2)|^2 = 1/2 = 50%
# P(|1> = |+>) = |<+|1>|^2 = |1/sqrt(2)|^2 = 1/2 = 50%
# P(|+> = |+>) = |<+|+>|^2 = |1|^2         = 1   = 100%
# P(|-> = |+>) = |<-|+>|^2 = |0|^2         = 0   = 0%
#
# To simulate an X-axis measurement, apply Hadamard gate, then do a
# Z-axis measurment, since Quantum Computers can only measure
# difference between 2 physical states.
#
# S Gate:
# Rotation of pi/2 radians around Z-axis (quarter turn (90 degrees)).
# S = [ 1 0 ] = (exponential notation:) [ 1    0     ]
#     [ 0 i ]                           [ 0 e^i*pi/2 ]
# apply S Gate to Plus:
# S|+> = [ 1 0 ][ 1/sqrt(2) ] = [ 1/sqrt(2) ] = |+i>
#        [ 0 i ][ 1/sqrt(2) ]   [ i/sqrt(2) ]
# SS|+> = |->  so S Gate is not its own inverse, like previous gates
# SS = [ 1 0 ][ 1 0 ] = [ 1  0 ] = Z (Pauli-Z Gate)
#      [ 0 i ][ 0 i ]   [ 0 -1 ]
# To avoid 3 S Gates (3/4 turn) (which is valid), use S-Dagger Gate,
# which rotates 1/4 in opposite direction (-pi/2 radians):
# Sdagger = [ 1  0 ] = [ 1     0     ]
#           [ 0 -i ]   [ 0 e^-i*pi/2 ]
# Daggar is a symbol that looks like a cross, and represents conjugate
# transpose.
# SSdaggar = [ 1 0 ][ 1  0 ] = [ 1 0 ] = I (identity matrix)
#            [ 0 i ][ 0 -i ]   [ 0 1 ]
#
# T Gate:
# Rotate pi/4 radians (1/8 turn).
# T = [ 1    0     ]  Tdagger = [ 1    0      ]
#     [ 0 e^i*pi/4 ]            [ 0 e^i*pi/-4 ]
# (reminder:)
# S = [ 1    0     ]  Sdagger = [ 1    0      ]
#     [ 0 e^i*pi/2 ]            [ 0 e^i*pi/-2 ]
