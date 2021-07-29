import matplotlib.pyplot as plt
from astropy.table import Table
import matplotlib.patches as mpatches
import matplotlib.patches as patches
from astropy.coordinates import SkyCoord
from matplotlib.patches import Rectangle
import matplotlib.lines as mlines
import astropy.units as u

##########################################################################
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 2.0
mpl.rcParams['axes.edgecolor'] = 'white'

mpl.rcParams.update({'font.size': 15, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})


##########################################################################

open_clusters_summary = Table.read("OpenClusters_GaiaDR2_summary.csv")

glob_clusters_summary = Table.read("GlobularClusters_GaiaEDR3_summary.csv")


#####################################################################
img = plt.imread("Gaia_sky.png") # import the backgournd image

fig = plt.figure(figsize=(7, 7)) # create a figure object 
plt.rcParams.update({'font.size': 10})

ax0 = fig.add_subplot(111) # create "layer" with the background image
ax0.imshow(img) # call the background image
ax0.axis("off") # turnoff axis for this background layer

# Create a black Rectangle patch (for dramatic purposes)
# to make the background white, just comment everything that that is used to call this black rectangle and all the code used to transform axis, labels, and edges to white 
rect = Rectangle((-60,-40),810,400,lw=0,edgecolor='none',facecolor='black', zorder=-10, clip_on=False)
# Add the patch to the Axes
ax0.add_patch(rect)

# now create the "true" plot
ax = fig.add_subplot(111, projection="aitoff")
ax.set_facecolor("None")
plt.grid(True, lw=0.5)


# PLOT OPEN CLUSTERS
gal = SkyCoord(open_clusters_summary["GLON"], open_clusters_summary["GLAT"], frame='galactic', unit=u.deg)

plt.scatter(-gal.l.wrap_at('180d').radian, gal.b.radian, c='C0', s=2, zorder=-5, marker='o', alpha=1.0, label=r'Open clusters')
# IMPORTANT: the minus signs simply reflects the longitude axis, as usual (e.g., in TOPCAT this is standard)

# PLOT PLEIADES
name = open_clusters_summary["Cluster"]
gal = SkyCoord(open_clusters_summary["GLON"][name=='Melotte_22'], open_clusters_summary["GLAT"][name=='Melotte_22'], frame='galactic', unit=u.deg)

plt.scatter(-gal.l.wrap_at('180d').radian, gal.b.radian, c='C0', s=150, zorder=+3, marker='*', edgecolor='white', alpha=1.0, label=r'Pleiades')



# PLOT GLOBULAR CLUSTERS
gal = SkyCoord(glob_clusters_summary["GAL_LONG"], glob_clusters_summary["GAL_LAT"], frame='galactic', unit=u.deg)

plt.scatter(-gal.l.wrap_at('180d').radian, gal.b.radian, c='C1', s=10, zorder=+2, marker='o', alpha=1.0, label='Globular clusters')



# PLOT omega cen
name = glob_clusters_summary["Name"]
gal = SkyCoord(glob_clusters_summary["GAL_LONG"][name=='NGC_5139_oCen'], glob_clusters_summary["GAL_LAT"][name=='NGC_5139_oCen'], frame='galactic', unit=u.deg)

plt.scatter(-gal.l.wrap_at('180d').radian, gal.b.radian, c='C1', s=150, zorder=+3, marker='*', edgecolor='white', alpha=1.0, label=r'$\omega$ Cen')


plt.xlabel("Galactic longitude", fontsize=15, labelpad=20)
plt.ylabel("Galactic latitude", fontsize=15)
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')


handles = []

handles.append(mlines.Line2D([],[], color='C0', alpha=1., linestyle='none', markeredgewidth=0, markeredgecolor='none', label=r"Globular clusters", marker='o', lw=2, markersize=10))

legend = plt.legend(facecolor='white', frameon=True, fontsize=10, framealpha=0.0, loc='upper left', bbox_to_anchor=(0.95, 1.1))
plt.setp(legend.get_texts(), color='white')

### SAVE AND LEAVE
plt.savefig("clusters_proj_sky_BLACK.png", dpi=600, bbox_inches='tight')



# LET'S MAKE THE SAME THING WITH THE WITHE BACKGROUND. MAYBE THIS IS USEFUL FOR SOMEONE
mpl.rcParams['axes.edgecolor'] = 'black'

#####################################################################
fig = plt.figure(figsize=(7, 7)) # create a figure object 
plt.rcParams.update({'font.size': 10})

ax0 = fig.add_subplot(111) # create "layer" with the background image
ax0.imshow(img) # call the background image
ax0.axis("off") # turnoff axis for this background layer

# now create the "true" plot
ax = fig.add_subplot(111, projection="aitoff")
ax.set_facecolor("None")
plt.grid(True, lw=0.5)


# PLOT OPEN CLUSTERS
gal = SkyCoord(open_clusters_summary["GLON"], open_clusters_summary["GLAT"], frame='galactic', unit=u.deg)

plt.scatter(-gal.l.wrap_at('180d').radian, gal.b.radian, c='C0', s=2, zorder=-5, marker='o', alpha=1.0, label=r'Open clusters')
# IMPORTANT: the minus signs simply reflects the longitude axis, as usual (e.g., in TOPCAT this is standard)

# PLOT PLEIADES
name = open_clusters_summary["Cluster"]
gal = SkyCoord(open_clusters_summary["GLON"][name=='Melotte_22'], open_clusters_summary["GLAT"][name=='Melotte_22'], frame='galactic', unit=u.deg)

plt.scatter(-gal.l.wrap_at('180d').radian, gal.b.radian, c='C0', s=150, zorder=+3, marker='*', edgecolor='black', alpha=1.0, label=r'Pleiades')



# PLOT GLOBULAR CLUSTERS
gal = SkyCoord(glob_clusters_summary["GAL_LONG"], glob_clusters_summary["GAL_LAT"], frame='galactic', unit=u.deg)

plt.scatter(-gal.l.wrap_at('180d').radian, gal.b.radian, c='C1', s=10, zorder=+2, marker='o', alpha=1.0, label='Globular clusters')



# PLOT omega cen
name = glob_clusters_summary["Name"]
gal = SkyCoord(glob_clusters_summary["GAL_LONG"][name=='NGC_5139_oCen'], glob_clusters_summary["GAL_LAT"][name=='NGC_5139_oCen'], frame='galactic', unit=u.deg)

plt.scatter(-gal.l.wrap_at('180d').radian, gal.b.radian, c='C1', s=150, zorder=+3, marker='*', edgecolor='black', alpha=1.0, label=r'$\omega$ Cen')


plt.xlabel("Galactic longitude", fontsize=15, labelpad=20)
plt.ylabel("Galactic latitude", fontsize=15)


handles = []

handles.append(mlines.Line2D([],[], color='C0', alpha=1., linestyle='none', markeredgewidth=0, markeredgecolor='none', label=r"Globular clusters", marker='o', lw=2, markersize=10))

legend = plt.legend(facecolor='black', frameon=True, fontsize=10, framealpha=0.0, loc='upper left', bbox_to_anchor=(0.95, 1.1))
plt.setp(legend.get_texts(), color='black')

### SAVE AND LEAVE
plt.savefig("clusters_proj_sky_WHITE.png", dpi=600, bbox_inches='tight')

