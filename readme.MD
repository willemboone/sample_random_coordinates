# random coordinate sampling

For one of my projects I needed to sample latitude/longitude coordinates all over the globe. 
Simple but incorrect, one could sample random numbers in[-180; 180] and [-90, 90]. 
However, this will cause the point cloud to be overly dense on the polar areas, because of area deformation. 

A better method is to use random sampling in cartesian (3d) globe environment and reproject those to lat/lon coordinates. 
The difference can be seen in figures random_points.png and random_points_incorrect.png. 
The functions for random lat/lon can be found in random_on_sphere.py.

Furthermore i wanted only to select points above land, so i used a shapefile containing polygons of all nations for this. 
The code for random lat/lon above land can be found in random_points_in_shp.py. 