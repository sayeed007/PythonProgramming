import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c = colors)   #Different color for each point

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100])

plt.scatter(x, y, c = colors, cmap='viridis', s = 5, alpha = 0.5)
# s = size of dot & alpha = Transparacy 
'''
Using ColorMap
cmap has other value like:
Accent		 	Accent_r	Blues		 	Blues_r	    BrBG		 	BrBG_r	    BuGn		 	BuGn_r	
BuPu		 	BuPu_r	    CMRmap		 	CMRmap_r	Dark2		 	Dark2_r	    GnBu		 	GnBu_r	
Greens		 	Greens_r	Greys		 	Greys_r	    OrRd		 	OrRd_r	Oranges		 	Oranges_r	
PRGn		 	PRGn_r	Paired		 	Paired_r	Pastel1		 	Pastel1_r	Pastel2		 	Pastel2_r	
PiYG		 	PiYG_r	PuBu		 	PuBu_r	PuBuGn		 	PuBuGn_r	PuOr		 	PuOr_r	
PuRd		 	PuRd_r	    Purples		 	Purples_r	RdBu		 	RdBu_r	    RdGy		 	RdGy_r	
RdPu		 	RdPu_r	    RdYlBu		 	RdYlBu_r	
RdYlGn		 	RdYlGn_r	Reds		 	Reds_r	Set1		 	Set1_r	Set2		 	Set2_r	Set3		 	Set3_r	
Spectral		 	Spectral_r	Wistia		 	Wistia_r	YlGn		 	YlGn_r	YlGnBu		 	YlGnBu_r	
YlOrBr		 	YlOrBr_r	YlOrRd		 	YlOrRd_r	afmhot		 	afmhot_r	autumn		 	autumn_r	binary		 	binary_r	
bone		 	bone_r	    brg		 	brg_r	    bwr		 	bwr_r	cividis		 	cividis_r	    cool		 	cool_r	
coolwarm		 	coolwarm_r	    copper		 	copper_r	cubehelix		 	cubehelix_r	    flag		 	flag_r	
gist_earth		 	gist_earth_r	gist_gray		 	gist_gray_r	    gist_heat		 	gist_heat_r	    gist_ncar		 	gist_ncar_r	
gist_rainbow		 	gist_rainbow_r	    gist_stern		 	gist_stern_r	gist_yarg		 	gist_yarg_r	    gnuplot		 	gnuplot_r	
gnuplot2		 	gnuplot2_r	gray		 gray_r	hot		 	hot_r	    hsv		 	hsv_r	    inferno		 	inferno_r	
jet		 	jet_r	    magma		 	magma_r	    nipy_spectral		 	nipy_spectral_r	    ocean		 	ocean_r	
pink		 pink_r	    plasma		 	plasma_r	prism		 	prism_r	    rainbow		 	rainbow_r	
seismic		 seismic_r	spring		 	spring_r	summer		 	summer_r	tab10		 	tab10_r	    
tab20		 tab20_r	    tab20b		 	tab20b_r	tab20c		 	tab20c_r	terrain		 	terrain_r	    
twilight	twilight_r	 twilight_shifted		 	twilight_shifted_r	    viridis		 	viridis_r	    winter		 	winter_r
'''
plt.colorbar()
#Ploting the Colorbar
plt.show()

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()