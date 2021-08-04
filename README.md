# Star_cluster_distribution
In this repository, I provide Python tools for plotting the **distribution of open and globular clusters** on the sky.

After quite a bit of searching, I was not able to find a figure that would provide a clear demonstration of the differences between the distribution of open and globular clusters in the Galaxy. Therefore, I used **data from the Gaia space mission** to create my own plot. 

I hope this is useful to some people. **Feel free to utilize the codes presented in this repository** for educational purposes, presentation/outreach, and even publications. Please acknowledge, if possible. (:
 
The background image that I utilize for these figure has been produced by ESA's Gaia Collaboration with data from its second data release. You can find it in the following link: [Gaia highlights](https://www.cosmos.esa.int/web/gaia/highlights-of-gaia-dr2). Please acknowledge their magnificent work. For details about how this image came to be and all that it represents, see, for instance, this other link: [Gaia sky map details](https://sci.esa.int/web/gaia/-/60169-gaia-s-sky-in-colour).

![Gaia sky map in colors](https://www.cosmos.esa.int/documents/29201/1666086/GDR2_fluxRGB_hammer_624x312.png/289bee74-9b94-3711-1538-487ff9513e61?t=1524433274000)

Overall, you can find all necessary information about the Gaia mission here: [Gaia mission](https://www.cosmos.esa.int/web/gaia). Verification papers from the Gaia Collaboration are also available (from all data releases) with open access: [NASA/ADS link](https://ui.adsabs.harvard.edu/search/filter_author_facet_hier_fq_author=AND&filter_author_facet_hier_fq_author=author_facet_hier:%220/Gaia%20Collaboration%22&fq=%7B!type=aqp%20v=$fq_author%7D&fq_author=(author_facet_hier:%220/Gaia%20Collaboration%22)&q=author:%22%5EGaia%20Collaboration%22&sort=date%20desc,%20bibcode%20desc&p_=0).

Furthermore, the open cluster compilation that I utilize also relies on data from Gaia's second data release. It contains ~1200 open clusters, including some that were discovered in this same article.

* [***Cantat-Gaudin** et al. 2018, **A&A**, 618, A93*](https://www.aanda.org/articles/aa/full_html/2018/10/aa33476-18/aa33476-18.html)

Attention. the nominal values for the positions (right ascension and declination) have NOT been updated with new data from Gaia.

Regarding globular clusters, I used the most recent catalog (with ~170 objects of such kind) constructed with data from Gaia's early data release 3.

* [***Vasiliev & Baumgardt** et al. 2021, **MNRAS**, 505, 5978*](https://doi.org/10.1093/mnras/stab1475)

The final figure is the following (there is also a version with black background available):

![clusters_map](https://raw.githubusercontent.com/guilhermelimberg/Star_cluster_distribution/main/clusters_proj_sky_WHITE.png)

Necessary [Python](https://www.python.org) libraries and packages: [matplotlib](https://matplotlib.org) and [Astropy](https://www.astropy.org).

You should be able to immediately run the code to produce the figures yourself by typing "python3 proj_clusters_in_Galaxy.py" in a terminal within the downloaded (and unzipped) folder.
