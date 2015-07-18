import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch
lista_arquivos=[]
LISTA=[]

k=''

grass.read_command('v.build',map='quadricula_nomeadas_shp@PERMANENT')
for i in range(51):
    i=i+1
    ond="cat="+`i`   
    apoio=grass.read_command('v.db.select', flags='c', map='quadricula_nomeadas_shp@PERMANENT', column='controle', where=ond,verbose=False)
    
    apoio=apoio.replace("\n",'')
    apoio=apoio.replace(" ",'')
    LISTA.append(apoio)


for i in LISTA:
    #grass.run_command('v.build.all')
    query="grade=\'"+i+"\'" 
    x=grass.read_command('v.db.select', flags='c', map='quadricula_nomeadas_shp@PERMANENT', column='NM_image', where=query,verbose=False) 
    grass.run_command('v.extract', input='quadricula_nomeadas_shp@PERMANENT', output='temp', where=query, type='area', new=1,overwrite=True,verbose=False) 
    grass.run_command('v.to.rast', input='temp', out='temp_rast_masc', use="cat",overwrite=True,verbose=False) 
    #print x 
    type(k)
    k=x.replace("\n","") 
    k=k.replace('\'',"")
    
    k=str(k)
    type(k)
    cont=0 
    #print a
    print k
    c=str(k)
    print c
    
    
    #print ">>>", k
    #print ">>>", c
    lista_arquivos=[]
    for root, dirs, files in os.walk('F:/data/john_pc2/rogerio/Imagens_Rapid_Eye_Canastra'):
        
        for file in files:
            if file.endswith(k):
                #print os.path.join(root, file)
                lista_arquivos.append(os.path.join(root, file)) 
                #print len(lista_arquivos)
                print lista_arquivos
                if (len(lista_arquivos)>1):
                    
                    #print "MENSAGEM FORAM ENCONTRADOS :",lista_arquivos, "UTILIZANDO O PRIMEIRO"
                                                x=0
    grass.run_command ('r.in.gdal', flags='o' ,input=lista_arquivos[0], output=i ,overwrite=True, verbose = False)    
    #grass.run_command('g.region', rast=i+'.1',verbose=False) 
    #grass.run_command('i.group', group=i ,subgroup=i,  input=i+'.3' ',' +i+'.4' ',' +i+'.5',verbose=False)    