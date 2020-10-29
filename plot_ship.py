#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cartopy.crs as ccrs
import cartopy
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.io.img_tiles import StamenTerrain
import numpy as np
import matplotlib.pyplot as plt
import shapely


# copy in coordinates from kml file by hand
way_points=[-3.410951578878632,50.61226419338077,
            -3.408957782258618,50.60897268488223,
            -3.407537907632134,50.60739408303765,
            -3.40321606837945,50.6052338416737,
            -3.399604321225697,50.60249905358306,
            -3.396767612167895,50.59716907677993,
            -3.396760420019268,50.59687275388968,
            -3.376705977263084,50.53895152125083,
            -3.368105383284451,50.50104482206139,
            -3.364817591113707,50.36777484388921,
            -3.341628900523813,50.2527598087858,
            -3.368197150986449,50.22640776349823,
            -3.314404891266713,50.10516017852498,
            -3.324371600596198,50.0963674741249,
            -3.367603755952259,49.92190869026717,
            -3.561668793554664,48.93522360883228,
            -4.202414259446826,48.79866074372679,
            -4.89631972469489,48.55483944497286,
            -5.226684771733211,48.44399477903798,
            -5.264736444275475,47.99390045003092,
            -4.785597172512492,47.73540875601405,
            -4.205635150607019,47.46193648655871,
            -3.821853371742113,47.26779984040011,
            -3.399190097132281,47.08666136903867,
            -3.10372340208338,46.90239683032956,
            -2.789384979069449,46.73132363093356,
            -2.768050424794748,46.68812006398098,
            -2.453940247323293,46.34166232239043,
            -2.122070113642105,45.96332715059899,
            -2.080767612357305,45.9048643311915,
            -1.548820118707565,45.21208240704152,
            -1.589800936318876,44.11145099143379,
            -1.907690517719757,43.44897489236993,
            -4.261794461452862,43.62751627613608,
            -5.384751430176163,43.7293292353858,
            -6.930089101069409,43.7005720893452,
            -8.306382247805026,43.95776384513615,
            -9.374114090621161,43.50293090701762,
            -9.68620279457255,42.71360176782028,
            -9.348768156828864,42.1032915860897,
            -9.366435877204777,42.05154371732696,
            -9.113664934059322,41.0245256844852,
            -9.222059605437449,40.98186203465954,
            -9.315437434787116,40.23951162931537,
            -9.69571536397685,39.16519777496757,
            -9.61502188855364,38.36160915432853,
            -9.306313845684254,37.99934734653008,
            -9.415995890583119,36.9047036774523,
            -8.879304726893952,36.56708858167121,
            -7.880574832069139,36.53671292478523,
            -7.096103861625135,36.36385695371247,
            -6.362222818036174,35.99643571730281,
            -6.48860780059681,35.10402299618364,
            -7.262587830491745,34.2432098464618,
            -8.487537743989831,33.55810167903991,
            -9.388105111120129,32.79428931966675,
            -10.01296286288453,31.71023927111439,
            -10.39846959944119,30.26368996521102,
            -10.80765596767415,29.17880711352841,
            -12.50467941267975,28.4140439079053,
            -13.44195401942612,27.98076464656793,
            -13.95461001979698,27.82372736347864,
            -15.51907910776807,27.63883083829034,
            -17.21940000000000,28.10330000000000]

lat_route=way_points[1::2]
lon_route=way_points[0::2]

lat_exmouth=50.62
lon_exmouth=-3.4137

lat_la_gomera=28.1033 
lon_la_gomera=-17.2194

lat_boat=lat_exmouth
lon_boat=lon_exmouth

#define map extent
extent = [-20, 2.5, 25, 52.5]
extent2 = [-6, -2.5, 47.5, 51]

#create figure
fig = plt.figure(figsize=(10, 8))
fig.suptitle('Exmouth to La Gomera')

ax = fig.add_subplot(1, 2, 1, projection=ccrs.PlateCarree())

rivers_10m = cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '10m')
land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor=cfeature.COLORS['land'])
#pop_10m=cfeature.NaturalEarthFeature('cultural','populated_places','10m',edgecolor='face', facecolor='red')

ax.set_extent(extent, crs=ccrs.PlateCarree())
#ax.coastlines(resolution='50m')
ax.add_feature(land_10m)
#ax.add_feature(pop_10m)
#ax.add_feature(rivers_10m, facecolor='None', edgecolor='b', alpha=0.5)
#ax.add_feature(cfeature.BORDERS, linestyle=':')

lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.set_xticks([-20,-15,-10,-5, 0, 5])
ax.xaxis.set_major_formatter(lon_formatter)
ax.set_yticks([25,30,35,40,45,50])
ax.yaxis.set_major_formatter(lat_formatter)
ax.plot(lon_exmouth, lat_exmouth, marker='o', color='blue', markersize=4, alpha=0.7, transform=ccrs.PlateCarree())
ax.plot(lon_la_gomera, lat_la_gomera, marker='o', color='blue', markersize=4, alpha=0.7, transform=ccrs.PlateCarree())
ax.plot(lon_route,lat_route, ':',transform=ccrs.PlateCarree())
ax.plot(lon_boat, lat_boat, marker='o', color='red', markersize=8, alpha=0.7, transform=ccrs.PlateCarree())
ax.set_title('Expedition chart')


ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.PlateCarree())
#tiler = StamenTerrain()
#mercator = tiler.crs
#ax2.add_image(tiler, 6)
#ax2.coastlines(resolution='10m')
ax2.add_feature(land_10m)

lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax2.set_xticks([-20,-15,-10,-5, 0, 5])
ax2.xaxis.set_major_formatter(lon_formatter)
ax2.set_yticks([25,30,35,40,45,50])
ax2.yaxis.set_major_formatter(lat_formatter)
ax2.plot(lon_exmouth, lat_exmouth, marker='o', color='blue', markersize=4, alpha=0.7, transform=ccrs.PlateCarree())
ax2.plot(lon_la_gomera, lat_la_gomera, marker='o', color='blue', markersize=4, alpha=0.7, transform=ccrs.PlateCarree())
ax2.plot(lon_route,lat_route, ':',transform=ccrs.PlateCarree())
ax2.plot(lon_boat, lat_boat, marker='o', color='red', markersize=8, alpha=0.7, transform=ccrs.PlateCarree())
ax2.set_title('Chart of the day')
ax2.set_extent(extent2)



plt.show()
