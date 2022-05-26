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
        gate['probability'] = [1,0,0,0]
    elif gate_type == 1:
        gate['name'] = 'bitflip'
        gate['matrices'] = [mat0,mat1,zero_mat,zero_mat]
        gate['probability'] = [1-var,var,0,0]
    elif gate_type == 2:
        gate['name'] = 'bitphaseflip'
        gate['matrices'] = [mat0,zero_mat,mat2,zero_mat]
        gate['probability'] = [1-var,0,var,0]
    elif gate_type == 3:
        gate['name'] = 'phaseflip'
        gate['matrices'] = [mat0,zero_mat,zero_mat,mat3]
        gate['probability'] = [1-var,0,0,var]
    elif gate_type == 4:
        gate['name'] = 'depolarizing'
        gate['matrices'] = [mat0,mat1,mat2,mat3]
        gate['probability'] = [1-(3*var/4),var/4,var/4,var/4]
    elif gate_type == 5:
        gate['name'] = 'fully depolarizing'
        gate['matrices'] = [mat0,mat1,mat2,mat3]
        gate['probability'] = [1/4,1/4,1/4,1/4]
    
    return gate
    



