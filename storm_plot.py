'''

  Plot storm tracks

'''

# Load required modules

import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits.basemap as bm


# Load storm data

data = np.load('storm_track_slp.npz')
storms = data['storms']

# Plot storm tracks
# Regional zoom in on the NW Atlantic
plt.figure()
plt.clf()
proj = bm.Basemap(llcrnrlon=-110.,llcrnrlat=35.,urcrnrlon=-67.,urcrnrlat=60., projection='merc',lat_1=20.,lat_2=40.,lon_0=-60., resolution ='l',area_thresh=1000.)
proj.drawcoastlines(linewidth=0.5)
for ed in range(len(storms)):
    # Select for: cyclonic storms which exist solely during November-March
#    if (storms[ed]['type'] == 'cyclonic') * ((storms[ed]['month'][0] >= 11)+(storms[ed]['month'][0] <= 3)) * ((storms[ed]['month'][-1]>=11)+(storms[ed]['month'][-1] <= 3)) * (storms[ed]['year'][0] >= 2000) * (storms[ed]['year'][-1] <= 2021):
    if (storms[ed]['type'] == 'cyclonic'):
    	lonproj, latproj = proj(storms[ed]['lon'], storms[ed]['lat'])
     	plt.plot(lonproj, latproj, '-', linewidth=1, alpha=0.6)
     	print storms[ed]['lon'], storms[ed]['lat'], storms[ed]['type']
plt.title('Storm tracks (2021 Dec 8-18)')
plt.savefig('figures/storm_tracks_GreatLakes', bbox_inches='tight', pad_inches=0.05, dpi=300)

