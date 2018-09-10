from quaternion import Quaternion
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def rotate_cube(cube, rot):
    corners = [Quaternion(0, *c) for c in cube]
    qorners = [Quaternion.rotate(q, rot) for q in corners]
    return corners, qorners


def generate_cube():
    cube = np.mgrid[-1:2:2, -1:2:2, -1:2:2]
    cube = np.moveaxis(cube, 0, -1).reshape(-1, 3)
    return cube


def generate_rotations(t0, t1):
    rot0 = Quaternion.rotation(+np.pi/4, t0)
    rot1 = Quaternion.rotation(-np.pi/3, t1)
    return rot0, rot1


def generate_translations():
    t0 = np.array([5, -6, 4], dtype=np.float32)
    t1 = np.array([-4, 3, 2], dtype=np.float32)
    return t0, t1


def plot_quaternions(c0, q0, t0, c1, q1, t1):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for c, q in zip(c0, q0):
        ax.scatter(*c[1:], c='b')
        ax.scatter(*q[1:], c='g')

    for c, q in zip(c1, q1):
        ax.scatter(*c[1:], c='b')
        ax.scatter(*q[1:], c='g')

    l0 = np.vstack((t0, [0] * 3)).T
    l1 = np.vstack((t1, [0] * 3)).T

    ax.plot(*l0, linestyle='dashed', c='grey')
    ax.plot(*l1, linestyle='dashed', c='grey')

    ax.set_axis_off()
    ax.set_title('Quaternion rotations')
    plt.savefig('images/quaternions.png')


def main():
    cube = generate_cube()
    t0, t1 = generate_translations()
    rot0, rot1 = generate_rotations(t0, t1)

    c0, q0 = rotate_cube(cube + t0, rot0)
    c1, q1 = rotate_cube(cube + t1, rot1)
    plot_quaternions(c0, q0, t0, c1, q1, t1)


if __name__ == '__main__':
    main()
