import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import math
s = ctrl.TransferFunction.s
c=6.815
delta=0.65
x1e=0.15
L0=0.122
L1=0.025
a=1.2
k=1885
m=0.454
Ie=0.7


t=sym.symbols('t')
#Define time inteval
n_points=5000
t_final=20
t_span=np.linspace(0,t_final,n_points)
#Define input F(t)
input_t= 1
def pid(kp , ki , kd):
# This function constructs the transfer function of a PID
# controller with given parameters
    diff = ctrl.TransferFunction ([1, 0], 1)
    intgr = ctrl.TransferFunction (1, [1, 0])
    pid_tf = kp + kd * diff + ki * intgr
    return pid_tf
controller=pid(5,3000,1000)
# define transfer functions
GD=7/(s**3+436.4*s**2+7036*s+62030)
GS=1/(0.03*s+1)
GC=controller
G_cl=ctrl.feedback(GD,GS*GC,sign=-1)# closeloop tf = GD/1+GD*GS*GC
# simulation
result_x1bar=ctrl.forced_response(G_cl, t_span , input_t)
plt.grid()
#plot x1bar
plt.subplot(2,1,1)
plt.plot(result_x1bar.time, result_x1bar.outputs)
plt.xlabel('t')
plt.ylabel('x1bar(t)')
#plot x
plt.subplot(2,1,2)
plt.plot(result_x1bar.time, delta-x1e-result_x1bar.outputs)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()

