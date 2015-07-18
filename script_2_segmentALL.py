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

k=''

grass.read_command('v.build',map='quadricula_nomeadas_shp@PERMANENT')
os.chdir(r"F:\data\john_pc2\rogerio\Imagens_Rapid_Eye_Canastra\grass\saidas_area_geral")
for i in range(49):
    i=i+1
    ond="cat="+`i`  
    #print i
    #print ond
    apoio=grass.read_command('v.db.select', flags='c', map='quadricula_nomeadas_shp@PERMANENT', column='controle', where=ond,verbose=False)
    
    apoio=apoio.replace("\n",'')
    apoio=apoio.replace(" ",'')
    apoio_ofile=apoio.replace("-",'_')
    LISTA_ofile.append(apoio_ofile)
    LISTA.append(apoio)
#print LISTA


for i in range(49):
    
    print LISTA[i]
    grass.run_command('i.group', group=LISTA[i] ,subgroup=LISTA[i],  input=LISTA[i]+'.1' ',' +LISTA[i]+'.2' ',' +LISTA[i]+'.3',verbose=False)
    grass.run_command('g.region', rast=LISTA[i]+'.1',verbose=False) 
    grass.run_command('i.segment', group=LISTA[i],output=LISTA_ofile[i]+'_segment_thre025_min0200',threshold=0.25, minsize=200,overwrite=True)
    