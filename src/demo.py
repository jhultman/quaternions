from quaternion import Quaternion
import matplotlib.pyplot as plt
import numpy as np


def demo_quaternions():
    corners = [
        [+1, -1], [+1, +1],
        [-1, -1], [-1, +1],
    ]

    corners = [Quaternion(0, *c, 0) for c in corners]
    rot = Quaternion.euler_rotation([0, 0, np.pi / 4])
    qorners = [Quaternion.rotate(q, rot) for q in corners]
    return corners, qorners


def plot_quaternions(corners, qorners):
    fig, ax = plt.subplots()
    ax.scatter(0, 0, c='black')

    for c, q in zip(corners, qorners):
        ax.scatter(*c[1:3], c='b')
        ax.scatter(*q[1:3], c='g')

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_axis_off()
    ax.set_aspect('equal')

    plt.savefig('images/quaternions.png')


def main():
    corners, qorners = demo_quaternions()
    plot_quaternions(corners, qorners)


if __name__ == '__main__':
    main()
