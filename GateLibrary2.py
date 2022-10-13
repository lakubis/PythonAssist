import sympy as sp
import numpy as np


def amplitude_damping(prob_var, eta_val):
    #t_1 = sp.Symbol('t_1', positive = True, real = True)
    #t_2 = sp.Symbol('t_2', positive = True, real = True)
    #var = t_1/(1+t_1)
    #eta = t_2/(1+t_2)
    if type(prob_var) == str:
        var = sp.Symbol(prob_var, real = True, positive = True)
    elif type(prob_var) == float or type(prob_var) == int or type(prob_var) == np.float64:
        var = prob_var
    #var = sp.Symbol(prob_var, real = True, positive = True)
    if type(eta_val) == str:
        eta = sp.Symbol('eta', real = True, positive = True)
    elif type(eta_val) == float or type(eta_val) == int or type(eta_val) == np.float64:
        eta = eta_val
    #eta = sp.Symbol('eta', real = True, positive = True)
    gate = {}
    gate['name'] = 'amplitude_damping'
    gate['matrices'] = [sp.sqrt(var)*sp.Matrix([[1,0],[0,sp.sqrt(1-eta)]]),sp.sqrt(var) * sp.Matrix([[0,sp.sqrt(eta)],[0,0]]),sp.sqrt((1-var))* sp.Matrix([[sp.sqrt(1-eta),0],[0,1]]),sp.sqrt(1-var)*sp.Matrix([[0,0],[sp.sqrt(eta),0]])]
    return gate



def choose_gate(prob_var, gate_type = 0):
    if type(prob_var) == str:
        var = sp.Symbol(prob_var,real = True)
    elif type(prob_var) == float or type(prob_var) == int or type(prob_var) == np.float64:
        var = prob_var
    zero_mat = sp.Matrix([[0,0],[0,0]])
    mat0 = sp.Matrix([[1,0],[0,1]])
    mat1 = sp.Matrix([[0,1],[1,0]])
    mat2 = sp.Matrix([[0,-sp.I],[sp.I,0]])
    mat3 = sp.Matrix([[1,0],[0,-1]])
    gate = {}
    if gate_type == 0:
        gate['name'] = 'identity'
        gate['matrices'] = [mat0,zero_mat,zero_mat,zero_mat]
    elif gate_type == 1:
        gate['name'] = 'bitflip'
        gate['matrices'] = [sp.sqrt(1-var)*mat0,sp.sqrt(var)*mat1,zero_mat,zero_mat]
    elif gate_type == 2:
        gate['name'] = 'bitphaseflip'
        gate['matrices'] = [sp.sqrt(1-var)*mat0,zero_mat,sp.sqrt(var)*mat2,zero_mat]
    elif gate_type == 3:
        gate['name'] = 'phaseflip'
        gate['matrices'] = [sp.sqrt(1-var)*mat0,zero_mat,zero_mat,sp.sqrt(var)*mat3]
    elif gate_type == 4:
        gate['name'] = 'depolarizing'
        gate['matrices'] = [sp.sqrt(1-(3*var/4))*mat0,sp.sqrt(var/4)*mat1,sp.sqrt(var/4)*mat2,sp.sqrt(var/4)*mat3]
    elif gate_type == 5:
        gate['name'] = 'fully depolarizing'
        gate['matrices'] = [sp.Rational(sp.sqrt(1/4))*mat0,sp.Rational(sp.sqrt(1/4))*mat1,sp.Rational(sp.sqrt(1/4))*mat2,sp.Rational(sp.sqrt(1/4))*mat3]
    
    return gate
    

def print_gate(gate):
    full_gate = sp.Matrix([[0,0],[0,0]])
    for i in range(4):
        full_gate = full_gate + gate['matrices'][i]

    return full_gate

def vonNeumann(keys):
    von = 0
    for i in keys:
        if i == 0:
            von = von - 0
        else:
            von = von - i*sp.log(i,2)
    return von

def get_keys(Eigen_value):
    index = [k for k in Eigen_value]
    keys = []
    for i in index:
        for j in range(Eigen_value[i]):
            keys.append(i)
    return keys

pauli_gates = [sp.Matrix([[1,0],[0,1]]),sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.Matrix([[1,0],[0,-1]])]

