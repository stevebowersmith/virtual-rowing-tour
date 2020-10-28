#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import matplotlib.pyplot as plt

#Create latitude and longitude data
lat=np.array([43.53,43.49,43.45,43.42,43.39,43.38,43.37,43.37,43.38,43.4])
lon=np.array([-116.16,-116.17,-116.23,-116.29,-116.36,-116.44,-116.52,-116.6,-116.68,-116.76])


lat_exmouth=50.62
lon_exmouth=-3.4137

lat_la_gomera=28.1033 
lon_la_gomera=17.2194

#define map extent
extent = [-25, 5, 30, 54]

#define state borders
states_borders = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_0_countries',
        scale='50m',
        facecolor='none')

states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')


#create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
#Add features
ax.add_feature(cfeature.LAND)
ax.add_feature(states_provinces, edgecolor='gray')
ax.add_feature(states_borders, edgecolor='black')
#plot data

ax.plot(lon_exmouth, lat_exmouth, marker='o', color='red', markersize=12,
        alpha=0.7, transform=ccrs.PlateCarree())

ax.plot(lon,lat, 'o',transform=ccrs.PlateCarree())
ax.set_extent(extent)

plt.show()
