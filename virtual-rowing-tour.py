#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():

    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.feature as cf
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    import datetime as dt
    import sys

    sys.path.append(sys.path[0] + "/src")

    from src import kml2latlon
    from src import read_logbook
    from src import travel

    name_start = "Exmouth"
    name_finish = "La Gomera"
    ifile_kml = "routes/Exmouth_La_Gomera.kml"
    start_date = '2020-10-31'
    final_date = dt.date.today().strftime("%Y-%m-%d")
    date_2 = dt.datetime.strptime(final_date,'%Y-%m-%d') - dt.timedelta(days=1)
    
    lat_route, lon_route = kml2latlon(ifile_kml)

    distance, last_date = read_logbook("log/rowing.log")
    lat_boat, lon_boat, d1, d2, d3 = travel(distance, lat_route, lon_route)

    extent_1 = [-20, 2.5, 25, 52.5]
    xticks_1 = range(-180,180,5)
    yticks_1 = range(0,90,5)

    # ToDo set as function of boat position
    extent_2 = [-6.25, -1.75, 46.25, 50.25]
    xticks_2 = range(-20,5,1)
    yticks_2 = range(25,51,1)
    
    proj = ccrs.PlateCarree()

    fig = plt.figure(figsize=(10, 8))
    fig.suptitle(name_start + ' to ' + name_finish
                 + ' ({:.0f} km)'.format(d2/1000.) + ' \n'
                 + start_date + ' - ' + last_date)

    land_10m = cf.NaturalEarthFeature('physical',
                                      'land', '10m',
                                      edgecolor='face',
                                      facecolor=cf.COLORS['land'])

    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()

    ax1 = fig.add_subplot(1, 2, 1, projection=proj)

    ax1.add_feature(land_10m)
    ax1.set_xticks(xticks_1)
    ax1.set_yticks(yticks_1)
    ax1.set_extent(extent_1, crs=proj)
    ax1.xaxis.set_major_formatter(lon_formatter)
    ax1.yaxis.set_major_formatter(lat_formatter)
    ax1.plot(lon_route[0], lat_route[0], marker='o', color='blue',
              markersize=6, alpha=1.0, transform=proj)
    ax1.plot(lon_route[-1], lat_route[-1], marker='o', color='blue',
             markersize=5, alpha=0.7, transform=proj)
    ax1.plot(lon_route, lat_route, ':', linewidth=2, transform=proj)
    ax1.plot(lon_boat, lat_boat, marker='o', color='red',
             markersize=8, alpha=0.7, transform=proj)
    ax1.set_title('Distance from ' + name_start + ': '
                  + '{:.0f} km'.format(d1/1000.))

    ax2 = fig.add_subplot(1, 2, 2, projection=proj)
    ax2.add_feature(land_10m)
    ax2.coastlines(resolution='10m',color='gray', alpha=0.7)
    ax2.set_xticks(xticks_2)
    ax2.xaxis.set_major_formatter(lon_formatter)
    ax2.set_yticks(yticks_2)
    ax2.yaxis.set_major_formatter(lat_formatter)
    ax2.plot(lon_route[0], lat_route[0], marker='o', color='blue',
             markersize=4, alpha=0.7, transform=proj)
    ax2.plot(lon_route[-1], lat_route[-1], marker='o', color='blue',
             markersize=4, alpha=0.7, transform=proj)
    ax2.plot(lon_route, lat_route, ':', transform=proj)
    ax2.plot(lon_boat, lat_boat, marker='o', color='red',
             markersize=8, alpha=0.7, transform=proj)
        
    d1 = dt.datetime.strptime(final_date,'%Y-%m-%d') - dt.timedelta(days=1)
    distance, _ = read_logbook("log/rowing.log",
                         startdate=date_2.strftime('%Y-%m-%d'),
                         enddate=final_date)
    ax2.set_title('Distance since ' + date_2.strftime("%Y-%m-%d") + ": " +
                  '{:.0f} km'.format(distance/1000.))

    ax2.set_extent(extent_2)

    # plt.show()
    plt.savefig("plots/Exmouth_RC_virtual_row_winter_2020--2021.png")


if __name__ == "__main__":
    main()
