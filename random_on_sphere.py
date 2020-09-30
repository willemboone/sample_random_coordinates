import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
""" for the math look at https: // mathworld.wolfram.com / SpherePointPicking.html"""


def random_cartesian():
    """returns random cartesian coordinate on as sphere with radius 1"""
    while True:
        x1, x2 = np.random.uniform(-1, 1, 2)
        if not x1**2 + x2**2 >= 1:
            break
    x = 2 * x1 * math.sqrt((1 - x1**2 - x2**2))
    y = 2 * x2 * math.sqrt((1 - x1**2 - x2**2))
    z = 1 - 2 * (x1**2 + x2**2)
    return x, y, z


def test_random_cartesian():
    """test function of random cartesian
    visualizes a 3D plot"""
    # containers
    _x = []
    _y = []
    _z = []
    # generate cartesian sphere coordinates
    for i in range(1000):
        x, y, z = random_cartesian()
        _x.append(x)
        _y.append(y)
        _z.append(z)
    # Create plot
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection="3d")
    ax.scatter3D(_x, _y, _z, color="green")
    plt.title("random cartesian on sphere")
    plt.show()


def cartesian_to_geo(x, y, z):
    """converts cartesian coordinates to lat lon in degrees"""
    r = math.sqrt((x**2 + y**2 + z**2))
    lat = (math.pi/2) - math.acos(z / r)
    lon = math.atan2(y, x)
    return np.degrees(lat), np.degrees(lon)


def random_lat_lon():
    """generates a random lat lon coordinate starting from random cartesian coordinates on sphere
    then converts them to lat lon in degrees"""
    x, y, z = random_cartesian()
    lat, lon = cartesian_to_geo(x, y, z)
    return lat, lon


def test_random_lat_lon():
    """test function of random_lat_lon
    visualizes in a plot"""
    _lon = []
    _lat = []
    # generate cartesian sphere coordinates
    for i in range(1000):
        x, y, z = random_cartesian()
        lat, lon = cartesian_to_geo(x, y, z)
        _lon.append(lon)
        _lat.append(lat)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(_lon, _lat)
    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    plt.title("random lat/lon")
    plt.show()


if __name__ == "__main__":
    test_random_cartesian()
    test_random_lat_lon()

