# random coordinate sampling

For one of my project I needed to sample latitudelongitude coordinates all over the globe. 
Simple but incorrect one could sample random numbers in[-180; 180] and [-90, 90], however this is not correct. 
The point cloud will be overly dense on the polar areas because the area deformation. 

The correct method is to have random sampling in cartesian (3d) environment and reproject those to latlon coordinates. 
The difference can be seen in figures random_points.png and random_points_incorrect.png. 
The functions for random latlon can be found in random_on_sphere.py.

Furthermore i wanted only to select point above land, so i used a shapefile containing polygons of all nations for this. 
The code for random latlon above land can be found in random_points_in_shp.py. 