import sympy as sp



def choose_gate(prob_var, gate_type = 0):
    var = sp.Symbol(prob_var,real = True)
    #var0 = sp.Symbol(prob_var + '_0',real = True)
    #var1 = sp.Symbol(prob_var + '_1',real = True)
    #var2 = sp.Symbol(prob_var + '_2',real = True)
    #var3 = sp.Symbol(prob_var + '_3',real = True)
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
        gate['matrices'] = [(1-var)*mat0,var*mat1,zero_mat,zero_mat]
    elif gate_type == 2:
        gate['name'] = 'bitphaseflip'
        gate['matrices'] = [(1-var)*mat0,zero_mat,var*mat2,zero_mat]
    elif gate_type == 3:
        gate['name'] = 'phaseflip'
        gate['matrices'] = [(1-var)*mat0,zero_mat,zero_mat,var*mat3]
    elif gate_type == 4:
        gate['name'] = 'depolarizing'
        gate['matrices'] = [(1-(3*var/4))*mat0,(var/4)*mat1,(var/4)*mat2,(var/4)*mat3]
    elif gate_type == 5:
        gate['name'] = 'fully depolarizing'
        gate['matrices'] = [sp.Rational(1/4)*mat0,sp.Rational(1/4)*mat1,sp.Rational(1/4)*mat2,sp.Rational(1/4)*mat3]
    
    return gate
    

def print_gate(gate):
    full_gate = sp.Matrix([[0,0],[0,0]])
    for i in range(4):
        #print(gate['matrices'][i])
        full_gate = full_gate + gate['matrices'][i]

    return full_gate

def vonNeumann(keys):
    von = 0
    for i in keys:
        if i == 0:
            von = von - 0
        else:
            von = von - i*sp.log(i)
    return von
