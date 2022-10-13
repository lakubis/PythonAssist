#%%
import numpy as np
from numpy import pi, sin, cos, ceil, floor, linspace, outer, ones, size

#
def angle2cartes(theta, phi, r = 1):
    '''
    This is a function to convert from spherical to cartesian coordinates, given the angle, it will return the x, y, and z's
    '''
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return x,y,z

def div_phi(theta, partition):
    '''
    This is a function to divide the phi, given theta and number of partition, it'll give a bunch of vectors that lies in a circle with angle theta
    '''
    vectors = []
    for i in range(partition):
        x,y,z = angle2cartes(theta, i * (2*pi)/partition)
        vec = [x,y,z]
        vectors.append(vec)

    return vectors

def div_sphere(part_constant):
    '''
    let's do some interesting math to divide the sphere
    '''
    arc_length = pi/part_constant
    vectors = []
    for i in range(part_constant+1):
        theta = i*(pi/part_constant)
        #print(theta)
        if arc_length > 1e-5:
            circumference = sin(theta)*2*pi
            part_phi = int(floor(circumference/arc_length))
            vectors = vectors + div_phi(theta,part_phi)
        else:
            vectors = vectors + div_phi(theta,1)

    return vectors

def points2XYZ(points):
    X = []
    Y = []
    Z = []
    for point in points:
        X.append(point[0])
        Y.append(point[1])
        Z.append(point[2])

    return X,Y,Z

def draw_bloch(ax):
    #Define variables
    sphere_color = '#FFDDDD'
    sphere_alpha = 0.2
    frame_color = 'gray'
    frame_alpha = 0.2
    frame_width = 1
    font_size = 20
    font_color = 'black'

    xlpos = [1.4, -1.4]
    ylpos = [1.4, -1.4]
    zlpos = [1.4, -1.4]
    xlabel = ['$x$', '']
    ylabel = ['$y$', '']
    zlabel = [r'$\left|0\right>$', r'$\left|1\right>$']

    u = linspace(0, pi, 25)
    v = linspace(0, pi, 25)
    x = outer(cos(u), sin(v))
    y = outer(sin(u), sin(v))
    z = outer(ones(size(u)), cos(v))
    ax.plot_surface(x, y, z, rstride=2, cstride=2,
                               color=sphere_color, linewidth=0,
                               alpha=sphere_alpha)
    ax.plot_wireframe(x, y, z, rstride=5, cstride=5,
                                 color=frame_color,
                                 alpha=frame_alpha)
    ax.plot(1.0 * cos(u), 1.0 * sin(u), zs=0, zdir='z',
                       lw=frame_width, color=frame_color)
    ax.plot(1.0 * cos(u), 1.0 * sin(u), zs=0, zdir='x',
                       lw=frame_width, color=frame_color)

    u = linspace(-pi, 0, 25)
    v = linspace(0, pi, 25)
    x = outer(cos(u), sin(v))
    y = outer(sin(u), sin(v))
    z = outer(ones(size(u)), cos(v))
    ax.plot_surface(x, y, z, rstride=2, cstride=2,
                               color=sphere_color, linewidth=0,
                               alpha=sphere_alpha)
    ax.plot_wireframe(x, y, z, rstride=5, cstride=5,
                                 color=frame_color,
                                 alpha=frame_alpha)
    ax.plot(1.0 * cos(u), 1.0 * sin(u),
                       zs=0, zdir='z', lw=frame_width,
                       color=frame_color)
    ax.plot(1.0 * cos(u), 1.0 * sin(u),
                       zs=0, zdir='x', lw=frame_width,
                       color=frame_color)
    opts = {'fontsize': font_size,
                'color': font_color,
                'horizontalalignment': 'center',
                'verticalalignment': 'center'}
    ax.text(0, -xlpos[0], 0, xlabel[0], **opts)
    ax.text(0, -xlpos[1], 0, xlabel[1], **opts)

    ax.text(ylpos[0], 0, 0, ylabel[0], **opts)
    ax.text(ylpos[1], 0, 0, ylabel[1], **opts)

    ax.text(0, 0, zlpos[0], zlabel[0], **opts)
    ax.text(0, 0, zlpos[1], zlabel[1], **opts)

    span = linspace(-1.0, 1.0, 2)
    ax.plot(span, 0 * span, zs=0, zdir='z', label='X',
                       lw=frame_width, color=frame_color)
    ax.plot(0 * span, span, zs=0, zdir='z', label='Y',
                       lw=frame_width, color=frame_color)
    ax.plot(0 * span, span, zs=0, zdir='y', label='Z',
                       lw=frame_width, color=frame_color)


# %%

# %%
