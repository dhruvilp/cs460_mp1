import sys
import numpy as np
import matplotlib.pyplot as pyplt
import matplotlib.patches as mplt_patches

if __name__ == "__main__":

    # Retrieve file name for input data
    if len(sys.argv) < 5:
        print("Four arguments required: python kalman2d.py [datafile] [x1] [x2] [lambda]")
        exit()

    filename = sys.argv[1]
    x10 = float(sys.argv[2])
    x20 = float(sys.argv[3])
    scaler = float(sys.argv[4])

    # Read data
    lines = [line.rstrip('\n') for line in open(filename)]
    data = []
    for line in range(0, len(lines)):
        data.append(list(map(float, lines[line].split(' '))))

    # Print out the data
    print("The input data points in the format of 'k [u1, u2, z1, z2]', are:")
    for it in range(0, len(data)):
        print(str(it + 1) + ": ", end='')
        print(*data[it])

        x_p = np.matrix([[x10], [x20]])
        I_2 = np.zeros((2, 2))
        I_2[0, 0] = I_2[1, 1] = 1.0
        P_p = scaler * I_2
        Q = np.matrix([[10 ** (-4), 2 * (10 ** (-5))], [2 * (10 ** (-5)), 10 ** (-4)]])
        R = np.matrix([[10 ** (-2), 5 * (10 ** (-3))], [5 * (10 ** (-3)), 2 * (10 ** (-2))]])
        x1 = []
        x2 = []
        z1 = []
        z2 = []
        for k in range(0, len(data)):
            line_k = data[k]
            u_p = np.matrix([[line_k[0]], [line_k[1]]])
            z_c = np.matrix([[line_k[2]], [line_k[3]]])

            x_ps = x_p + u_p
            P_ps = P_p + Q

            K_c = P_ps * np.linalg.inv(P_ps + R)
            x_c = x_ps + np.dot(K_c, (z_c - x_ps))
            P_c = (I_2 - K_c) * P_ps
            x1.append(x_c[0, 0])
            x2.append(x_c[1, 0])
            z1.append(z_c[0, 0])
            z2.append(z_c[1, 0])
            P_p = P_c
            x_p = x_c
        pyplt.figure()
        pyplt.plot(x1, x2, 'r', zorder=1, lw=3, color='red')
        pyplt.scatter(x1, x2, s=40, zorder=2, color='red')
        pyplt.plot(z1, z2, 'r', zorder=1, lw=3, color='green')
        pyplt.scatter(z1, z2, s=40, zorder=2, color='green')
        red_p = mplt_patches.Patch(color='red', label='xk(Calculated)')
        green_p = mplt_patches.Patch(color='green', label='zk(Observed)')
        pyplt.legend(handles=[red_p, green_p])
        pyplt.show()
