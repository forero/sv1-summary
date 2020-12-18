# script to read the tile_nights_exposures.json file and find
# all tiles, nights and exposures that included QSOs in the targets.

import json

f = open("tile_nights_exposures.json", "r")
obs = json.load(f) # this is a list of tiles with their SV1 observations
f.close()

target  = "QSO" # this is the type of targets I am looking for

tileid_nightid_tileid = []
for tile in obs: # loop over the list of tiles
    tileid = tile["tileid"]
    if target in tile["targets"]: # check that "QSO" is included in the targets
        for night in tile["nights"]: # iterate over the list of nights
            # make a new string that combines tileid_nightid_expid
            s = [str(tileid)+"_"+str(night["nightid"])+'_'+str(i) for i in night["expid"]]
            tileid_nightid_tileid += s

#print the list of tileid_nightid_tileid
for t in tileid_nightid_tileid:
    print(t)
