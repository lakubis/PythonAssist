#%%
from sympy import Matrix, Symbol, I, N, evalf
from sympy.physics.quantum import Dagger

def point2rho(point):
    rho = (1/2)*Matrix([[point[2] + 1, point[0] - I*point[1]],[point[0] + I*point[1], 1-point[2]]])
    return rho

def rho2point(rho):
    x = rho[0,1] + rho[1,0]
    y = (rho[1,0] - rho[0,1])/I
    z = rho[0,0] - rho[1,1]
    point = [complex(x),complex(y),complex(z)]
    return point
    
def transform_points(points, gates):
    trans_points = []
    for point in points:
        rho = point2rho(point)
        trans_rho = Matrix([[0,0],[0,0]])
        for gate in gates['matrices']:
            trans_rho = trans_rho + gate*rho*Dagger(gate)
        trans_point = rho2point(trans_rho)
        trans_points.append(trans_point)

    return trans_points

# %%
