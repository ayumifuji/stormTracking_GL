import numpy as np
from netCDF4 import Dataset,num2date
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfea
import matplotlib.pyplot as plt

projection=ccrs.PlateCarree()

nc = Dataset('data/era5_data_3hr_ver2.nc','r')
lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
time = nc.variables['time'][:]
timeunit = nc.variables['time'].units
msl = (nc.variables['msl'][:,:])
nc.close()


# read npz file
data = np.load('storm_det_slp.npz',allow_pickle=True,encoding='latin1')
storms = data['storms']
hour = data['hour']
day  = data['day']
#for ed in range(len(storms)):
#	print ed,storms[ed]['type'],hour[ed]	
#	for tt in range(len(storms[ed]['hour'])):
#		if storms[ed]['day'][tt] == 11 and storms[ed]['hour'][tt] == 18:
		#	print ed,tt,storms[ed]['lon'][tt],storms[ed]['lat'][tt],storms[ed]['day'][tt],storms[ed]['hour'][tt]

date_tmp = num2date(time,timeunit,calendar = "gregorian")  

print(lon.min(),lon.max(),lat.min(),lat.max())
lon,lat=np.meshgrid(lon,lat)

for ii in range(len(time)):

	fig=plt.figure()
	ax=fig.add_subplot(1,1,1,projection=projection)
	ax.set_extent([lon.min(),lon.max(),lat.min(),lat.max()],projection)
	ax.add_feature(cfea.COASTLINE,lw=.5)
	ax.add_feature(cfea.LAKES,alpha=0.3,lw=.5)
	#ax.coastlines(resolution='10m')
	pc=ax.pcolor(lon,lat,msl[ii,:,:]/100,cmap='rainbow',vmin=980,vmax=1040)
	ax.set_title('mean sea level pressure [hPa] '+str(date_tmp[ii]),loc='left',fontsize=9)
	fig.colorbar(pc,shrink=0.7,extend='both')
	#plt.show()

	for ed in range(len(storms)):
		#print storms[ed], len(storms[ed]['lon']), storms[ed]['N']
		#exit()
		for nl in range(storms[ed]['N']):
                		if day[ed] == date_tmp[ii].day and hour[ed] == date_tmp[ii].hour:
                                        print(ed, nl, str(date_tmp[ii]), day[ed], hour[ed])
                                        if storms[ed]['type'][nl] == 'anticyclonic':
                                                ax.scatter(storms[ed]['lon'][nl],storms[ed]['lat'][nl],color='red')
                                        elif storms[ed]['type'][nl] == 'cyclonic':
                                                ax.scatter(storms[ed]['lon'][nl],storms[ed]['lat'][nl],color='blue')
                                        else:
                                                print('Invalid storm type, ', storms[ed]['type'][nl], ed, tt, nl)
	#				ax.scatter(storms[ed]['lon'][tt],storms[ed]['lat'][tt],color='black')

	fig.savefig('figures/msl_maps/msl_det_'+str(date_tmp[ii]).replace(" ","_").replace(":","")+'.png',dpi=200)
	plt.close()


