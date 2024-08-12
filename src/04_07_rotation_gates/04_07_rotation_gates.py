from math import pi
from qiskit import *
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import StatevectorSimulator
#%matplotlib inline

circuit = QuantumCircuit(3)
circuit.rx(pi/3, 0)  # angle of pi/3 on zeroth qubit
circuit.ry(pi/3, 1)
circuit.h(2)
circuit.rz(pi/3, 2)
circuit.draw(output='mpl')

simulator = StatevectorSimulator()
result = simulator.run(circuit).result()
plot_bloch_multivector(result.get_statevector())

# Notes:
# Parameterized Rotation Operators
# - rotate a specified angle around X, Y, or Z axis of Bloch sphere
# - represented R sub X, R sub Y, or R sub Z, which indicate number of
#   radians of rotation
# RX(theta) = [    cos(theta/2) -i*sin(theta/2) ]  where theta is the
#             [ -i*sin(theta/2)    cos(theta/2) ]  angle to rotate on
# RY(theta) = [    cos(theta/2)   -sin(theta/2) ]  Bloch sphere from
#             [    sin(theta/2)    cos(theta/2) ]  |0>
#
# RZ(phi) = [ e^-i*phi/2    0      ]  where phi is angle around Z,
#           [     0      e^i*phi/2 ]  which only affects phase
#
# similarity to Pauli Gates (insert angle of pi):
# RX(pi) = [    cos(pi/2) -i*sin(pi/2) ] = [  0 -i ] = -i [ 0 1 ] = -iX
#          [ -i*sin(pi/2)    cos(pi/2) ]   [ -i  0 ]      [ 1 0 ]
# RY(pi) = [    cos(pi/2)   -sin(pi/2) ] = [ 0 -i ] = i [ 0 -i ] = iY
#          [    sin(pi/2)    cos(pi/2) ]   [ 1  0 ]     [ i  0 ]
#
# RZ(pi) = [ e^-i*pi/2    0      ] = [ -i 0 ] = -i [ 1  0 ] = -iZ
#          [     0      e^i*pi/2 ]   [  0 i ]      [ 0 -1 ]
#
# The imaginary numbers above multiplied to Pauli Gates don't affect
# in an observable way.
