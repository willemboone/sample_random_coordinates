from shapely.geometry import Point
import random
import geopandas as gp
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from random_on_sphere import random_lat_lon
import numpy as np


class RandomPoints(object):
    def __init__(self, shp, start_date, end_date):
        """generates random points within a shapefile
        :param shp: String to file location of polygon in which points need to be created
        :param start_date: datetime object
        :param end_date: datetime object
        """
        self.start_date = start_date
        self.end_date = end_date
        self.aoi = gp.read_file(shp)
        # merge the polygons of the shapefile into one area of interest, this takes some time
        print("merging the polygons in the shapefile to a single shape, this might take a while...")
        self.aoi_geom = self.aoi.unary_union
        self.points_df = pd.DataFrame(columns=["lat", "lon", "random_date"])
        self.points_list = []
        print("object initialized")

    def create_points(self, count):
        """
        :param count: integer, number of points to create
        :return: self.point, pandas dataframe
        """
        counter = 0
        while counter < count:
	    lat, lon = random_lat_lon()
            p = Point(lon, lat)
            if self.aoi_geom.contains(p):
                print("point added {}".format(counter + 1))
                random_date = self.random_date()
                self.points_df = self.points_df.append({"lat": lat, "lon": lon, "random_date": random_date}, ignore_index=True)
                self.points_list.append(p)
                counter += 1

    def random_date(self):
        """generates a random date within the range defined in the object"""
        start_date = self.start_date.toordinal()
        end_date = self.end_date.toordinal()
        random_day = dt.date.fromordinal(random.randint(start_date, end_date))
        return random_day

    def visualize(self):
        gs = gp.GeoSeries(self.points_list)
        fig, ax = plt.subplots()
        self.aoi.plot(ax=ax, facecolor='none', edgecolor='steelblue')
        gs.plot(ax=ax, color='r')
        plt.show()

    def save_df(self, path):
        self.points_df.to_csv(path)


if __name__ == "__main__":
    start = dt.datetime(year=2018, month=1, day=1)
    end = dt.datetime(year=2018, month=12, day=31)
    RP = RandomPoints("D:/paper/shp/World_countries/World_countries.shp", start, end)
    t0 = dt.datetime.now()
    RP.create_points(1000)
    t1 = dt.datetime.now()
    print("computing time: {}".format(t1-t0))
    RP.visualize()




