import fitsio

cols = ['expid', 'night', 'tileid', 'exptime', 'airmass_med', 'moon_sep_deg_med', 
       'transparency_med', 'fwhm_asec_med', 'sky_mag_ab_med', 'fiber_fracflux_med', 
        'ebv', 'b_depth', 'r_depth','z_depth' ]

data = fitsio.read('desi_sv1_exposures_gfa_with_depth.fits', columns=cols)

c = '||'
for col in cols:
    c += col+'||'
n = len(data)
print(c)
for i in range(n):
    l = str(data[i][cols])
    l =l.replace(",","||")
    l = l.replace("(", "||")
    l = l.replace(")", "||")
    print(l)