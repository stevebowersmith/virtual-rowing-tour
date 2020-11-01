#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def kml2latlon(ifile):

    """Read lon lat from kml file with single path"""

    from fastkml import kml, geometry

    with open(ifile, 'rt') as myfile:
        doc = myfile.read()
    k = kml.KML()
    k.from_string(doc.encode("utf-8"))
    f = list(k.features())
    g = list(f[0].features())[0].geometry

    lat = []
    lon = []
    for c in g.coords:
        lon.append(c[0])
        lat.append(c[1])

    return lat, lon


def read_logbook(ifile, startdate=None, enddate=None):
    """ ToDo: Write reader for logbook to return distance in m
        rowed between start and end date"""
    distance = 15000

    return distance


def coords2d(lat, lon):
    import shapely
    import numpy as np
    from cartopy import geodesic

    latlon = tuple(zip(lat, lon))
    myGeod = geodesic.Geodesic(6378137.0, 1/298.257223563)
    shapelyObject = shapely.geometry.LineString(list(latlon))
    s = myGeod.geometry_length(np.array(shapelyObject.coords))

    return s


def travel(distance, lat_route, lon_route):
    "ToDo: travel distance [m] along route and return position at destination"
    import shapely
    import numpy as np
    from cartopy import geodesic
    import sys

    # total length of route
    latlon = tuple(zip(lat_route, lon_route))
    myGeod = geodesic.Geodesic(6378137.0, 1 / 298.257223563)
    shapelyObject = shapely.geometry.LineString(list(latlon))
    # calculate length of path on ellipsoid
    s = myGeod.geometry_length(np.array(shapelyObject.coords))
    print("distance from start to finish is " + str(float(s)/1000.0) + " km")

    # distance to each waypoint
    
    s = 0.0

    s_vec = np.empty(len(lat_route))
    s_vec[:] = np.NaN
    
    s_sum = np.empty(len(lat_route))
    s_sum[:] = np.NaN
    
    for n in range(len(lat_route)):
        if n == 0:
            s = 0.0
            s_vec[n] = s
            s_sum[n] = s
        else:
            # row leg from waypoint n-1 to n
            s = coords2d([lat_route[n-1], lat_route[n]],
                         [lon_route[n-1], lon_route[n]])
            s_vec[n] = s
            s_sum[n] = s + s_sum[n-1]

        print(n)
        print(s_vec[n])
        print(s_sum[n])
        print ("----")

    # ToDo: Find last passed way point by comparing distance of
    #       waypoint with travled distance and return lon/lat


    
    # ToDo: Find additional stretch rowed once the last waypoint was passed

    # ToDo: Quality control (Check if parameters for geoid are consitent
    #       with google earth, try different routes, ...)

    lat_pos = -999
    lon_pos = -888

    return lat_pos, lon_pos


def main():

    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

    # Define start and finish

    lat_start = 50.62
    lon_start = -3.4137
    name_start = "Exmouth"

    lat_finish = 28.1033
    lon_finish = -17.2194
    name_finish = "La Gomera"

    # read planned route from kml file

    ifile_kml = "routes/route.kml"
    # ifile_kml = "routes/shortcut.kml"

    lat_route, lon_route = kml2latlon(ifile_kml)

    lon_route.insert(0, lon_start)
    lat_route.insert(0, lat_start)

    lon_route.append(lon_finish)
    lat_route.append(lat_finish)

    # read traveled distance in m
    distance = read_logbook("log/rowing.log",
                            startdate="2020-10-31",
                            enddate="2020-10-31")

    # Define position of boat

    lat_boat = lat_start
    lon_boat = lon_start

    lat_boat_test, lon_boat_test = travel(distance, lat_route, lon_route)

    # Create plot

    extent1 = [-20, 2.5, 25, 52.5]
    extent2 = [-6, -2.5, 47.5, 51]

    fig = plt.figure(figsize=(10, 8))
    fig.suptitle('Exmouth to La Gomera')

    rivers_10m = cfeature.NaturalEarthFeature('physical',
                                              'rivers_lake_centerlines', '10m')
    land_10m = cfeature.NaturalEarthFeature('physical',
                                            'land', '10m',
                                            edgecolor='face',
                                            facecolor=cfeature.COLORS['land'])

    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()

    ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.PlateCarree())
    ax1.set_extent(extent1, crs=ccrs.PlateCarree())
    # ax1.coastlines(resolution='50m')
    ax1.add_feature(land_10m)
    # ax1.add_feature(rivers_10m, facecolor='None', edgecolor='b', alpha=0.5)
    ax1.set_xticks([-20, -15, -10, -5, 0, 5])
    ax1.xaxis.set_major_formatter(lon_formatter)
    ax1.set_yticks([25, 30, 35, 40, 45, 50])
    ax1.yaxis.set_major_formatter(lat_formatter)
    ax1.plot(lon_start, lat_start, marker='o', color='blue',
             markersize=4, alpha=0.7, transform=ccrs.PlateCarree())
    ax1.plot(lon_finish, lat_finish, marker='o', color='blue',
             markersize=4, alpha=0.7, transform=ccrs.PlateCarree())
    ax1.plot(lon_route, lat_route, ':', transform=ccrs.PlateCarree())
    ax1.plot(lon_boat, lat_boat, marker='o', color='red',
             markersize=8, alpha=0.7, transform=ccrs.PlateCarree())
    ax1.set_title('Expedition chart')

    ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.PlateCarree())
    ax2.add_feature(land_10m)
    ax2.set_xticks([-20, -15, -10, -5, 0, 5])
    ax2.xaxis.set_major_formatter(lon_formatter)
    ax2.set_yticks([25, 30, 35, 40, 45, 50])
    ax2.yaxis.set_major_formatter(lat_formatter)
    ax2.plot(lon_start, lat_start, marker='o', color='blue',
             markersize=4, alpha=0.7, transform=ccrs.PlateCarree())
    ax2.plot(lon_finish, lat_finish, marker='o', color='blue',
             markersize=4, alpha=0.7, transform=ccrs.PlateCarree())
    ax2.plot(lon_route, lat_route, ':', transform=ccrs.PlateCarree())
    ax2.plot(lon_boat, lat_boat, marker='o', color='red',
             markersize=8, alpha=0.7, transform=ccrs.PlateCarree())
    ax2.set_title('Chart of the day')
    ax2.set_extent(extent2)

    plt.show()
    # plt.savefig("plots/Exmouth_RC_virtual_row_winter_2020--2021.pdf")
    # plt.savefig("plots/Exmouth_RC_virtual_row_winter_2020--2021.png")


if __name__ == "__main__":
    main()
