"""
    Exercise 8: Daylight map
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from time import gmtime, time, strftime


def R_x(phi):
    return np.matrix([
        [           1,           0,           0],
        [           0, np.cos(phi), np.sin(phi)],
        [           0,-np.sin(phi), np.cos(phi)],
    ])

def R_y(phi):
    return np.matrix([
        [ np.cos(phi),           0,-np.sin(phi)],
        [           0,           1,           0],
        [ np.sin(phi),           0, np.cos(phi)],
    ])

def R_z(phi):
    return np.matrix([
        [ np.cos(phi), np.sin(phi),           0],
        [-np.sin(phi), np.cos(phi),           0],
        [           0,           0,           1],
    ])

def get_sunlight_coverage_at_time(time, width=10, height=10):
    hour = time.tm_hour + time.tm_min / 60
    yday = time.tm_yday
    inclination = 23.4

    phi_day = (hour / 12 * np.pi) - np.pi
    phi_year = yday / 365 * 2 * np.pi
    phi_inc = inclination / 180 * np.pi

    e_sun = [1,0,0] * R_z(phi_year)

    M = np.matrix(np.zeros((width, height)))
    y = 0
    for phi_long in np.linspace(-np.pi, np.pi, width):
        x = 0
        for phi_lat in np.linspace(-np.pi/2, np.pi/2, height):
            e_loc = [1,0,0] * R_y(-phi_lat) * R_z(phi_long + phi_day + phi_year) * R_x(phi_inc)
            M[x,y] = np.dot(e_sun.A1, e_loc.A1)
            x += 1
        y += 1

    return M


if __name__ == '__main__':

    fig = plt.figure()
    axes = fig.add_subplot(1, 1, 1)

    image = imread("worldmap.png")

    t = time()
    while True:
        N = 30
        x = np.linspace(0, 800, N)
        y = np.linspace(0, 400, N)

        current_time = gmtime(t)
        z = get_sunlight_coverage_at_time(current_time, width=N, height=N)

        axes.clear()
        axes.title.set_text(strftime("%d.%m.%Y %H:%M", current_time))
        axes.imshow(image)
        axes.contourf(x, y, z, np.linspace(-1, 1, 10), cmap="hot", alpha=0.5)

        axes.xaxis.set_visible(False)
        axes.yaxis.set_visible(False)

        plt.pause(1/30)
        t += 60*60*24
