
import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch
lista_arquivos=[]
LISTA=[]
LISTA_ofile=[]
grass.read_command('v.build',map='quadricula_nomeadas_shp@PERMANENT')
os.chdir(r"F:\data\john_pc2\rogerio\Imagens_Rapid_Eye_Canastra\grass\saidas_area_geral")
for i in range(51):
    i=i+1
    ond="cat="+`i`   
    apoio=grass.read_command('v.db.select', flags='c', map='quadricula_nomeadas_shp@PERMANENT', column='controle', where=ond,verbose=False)
    
    apoio=apoio.replace("\n",'')
    apoio=apoio.replace(" ",'')
    apoio_ofile=apoio.replace("-",'_')
    LISTA_ofile.append(apoio_ofile)
    LISTA.append(apoio)


con=0
x=len(LISTA)
print LISTA
for i in LISTA:
    grass.run_command('g.region', rast=LISTA[con]+'.1',verbose=False)
    grass.run_command('r.to.vect', input=LISTA_ofile[con]+'_segment_thre025_min0200', out=LISTA_ofile[con]+'_segment_thre025_min0200_vect',feature='area',verbose=False,overwrite=True )
    grass.read_command('v.build',map=LISTA_ofile[con]+'_segment_thre025_min0200_vect')
    grass.run_command('v.rast.stats', vect=LISTA_ofile[con]+'_segment_thre025_min0200_vect',raster=LISTA[con]+'.1',colprefix='band1')
    grass.run_command('v.rast.stats', vect=LISTA_ofile[con]+'_segment_thre025_min0200_vect',raster=LISTA[con]+'.2',colprefix='band2')
    grass.run_command('v.rast.stats', vect=LISTA_ofile[con]+'_segment_thre025_min0200_vect',raster=LISTA[con]+'.3',colprefix='band3')
    grass.run_command('v.rast.stats', vect=LISTA_ofile[con]+'_segment_thre025_min0200_vect',raster=LISTA[con]+'.4',colprefix='band4')
    grass.run_command('v.rast.stats', vect=LISTA_ofile[con]+'_segment_thre025_min0200_vect',raster=LISTA[con]+'.5',colprefix='band5')
    grass.run_command('v.out.ogr', input=LISTA_ofile[con]+'_segment_thre025_min0200_vect', dsn=LISTA_ofile[con]+'_segment_thre025_min0200_vect.shp', type='area',verbose=False)  
    con=con+1