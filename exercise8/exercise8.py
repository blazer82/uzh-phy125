"""
    Exercise 8: Daylight map
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from time import gmtime, time, strftime
from dateutil import parser


def R_x(phi):
    """
    Return rotation matrix for x axis
    """
    return np.matrix([
        [           1,           0,           0],
        [           0, np.cos(phi), np.sin(phi)],
        [           0,-np.sin(phi), np.cos(phi)],
    ])

def R_y(phi):
    """
    Return rotation matrix for y axis
    """
    return np.matrix([
        [ np.cos(phi),           0,-np.sin(phi)],
        [           0,           1,           0],
        [ np.sin(phi),           0, np.cos(phi)],
    ])

def R_z(phi):
    """
    Return rotation matrix for z axis
    """
    return np.matrix([
        [ np.cos(phi), np.sin(phi),           0],
        [-np.sin(phi), np.cos(phi),           0],
        [           0,           0,           1],
    ])

def get_sunlight_coverage_at_time(time, width=10, height=10):
    """
    Return sunlight coverage matrix for a given time
    """

    # Define initial parameters
    hour = time.tm_hour + time.tm_min / 60
    yday = time.tm_yday
    inclination = 23.5

    # Calculate angles
    phi_day = (hour / 12 * np.pi) - np.pi
    phi_year = (yday / 365 * 2 * np.pi) - (np.pi / 365 * 172) # The second part is a correction term to approximate seasons
    phi_inc = np.radians(inclination)

    # Calculate sun vector
    e_sun = [1,0,0] * R_z(phi_year)

    # Initialize matrix
    M = np.matrix(np.zeros((width, height)))
    y = 0
    for phi_long in np.linspace(-np.pi, np.pi, width):
        x = 0
        for phi_lat in np.linspace(-np.pi/2, np.pi/2, height):
            # Calculate location vector
            e_loc = [1,0,0] * R_y(-phi_lat) * R_z(phi_long + phi_day + phi_year) * R_x(phi_inc)
            M[x,y] = np.dot(e_sun.A1, e_loc.A1)
            x += 1
        y += 1

    return M


if __name__ == '__main__':

    fig = plt.figure()
    axes = fig.add_subplot(1, 1, 1)

    # Read backround image
    image = imread("worldmap.png")

    # Set initial time
    t = parser.parse("2017-04-28 12:00:00 +0000").timestamp()

    # Plot and animate
    while True:
        N = 30
        x = np.linspace(0, 800, N)
        y = np.linspace(0, 400, N)

        current_time = gmtime(t)
        z = get_sunlight_coverage_at_time(current_time, width=N, height=N)

        axes.clear()
        axes.title.set_text(strftime("%d.%m.%Y %H:%M GMT", current_time))
        axes.imshow(image)
        axes.contourf(x, y, z, np.linspace(-1, 1, 10), cmap="hot", alpha=0.5)

        axes.xaxis.set_visible(False)
        axes.yaxis.set_visible(False)

        plt.pause(1/20)
        t += 60*30
