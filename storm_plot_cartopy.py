'''

  Plot storm tracks

'''

# Load required modules

import numpy as np
from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfea

# decide projection
projection=ccrs.PlateCarree()


# Load storm data
data = np.load('storm_track_slp.npz',allow_pickle=True,encoding='latin1')
storms = data['storms']


# Plot storm tracks
# Regional zoom in on the NW Atlantic
fig=plt.figure()
ax=fig.add_subplot(1,1,1,projection=projection)
ax.set_extent([-110.0,-67.0,35.0,60.0],projection)
ax.add_feature(cfea.COASTLINE,lw=.5)
ax.add_feature(cfea.LAKES,alpha=0.3,lw=.5)

for ed in range(len(storms)):
    # Select for: cyclonic storms 
    if (storms[ed]['type'] == 'cyclonic'):
        ax.plot(storms[ed]['lon'][:],storms[ed]['lat'][:],'-', linewidth=1, alpha=0.6)
        print(storms[ed]['lon'], storms[ed]['lat'], storms[ed]['type'])
plt.title('Storm tracks (2021 Dec 8-18)')
plt.savefig('figures/storm_tracks_GreatLakes', bbox_inches='tight', pad_inches=0.05, dpi=300)

