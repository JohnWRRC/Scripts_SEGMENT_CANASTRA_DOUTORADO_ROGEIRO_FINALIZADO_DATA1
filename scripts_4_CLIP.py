import arcpy
arcpy.env.overwriteOutput = True


grade="quadricula_nomeadas_editacao_manual"
arcpy.env.workspace=r"F:\data\john_pc2\rogerio\Imagens_Rapid_Eye_Canastra\grass\saidas_area_geral"
fc=arcpy.ListFeatureClasses()

lista="A-01","A-02","A-03","B-01","B-02","B-03","B-04","C-02","C-03","C-04","C-05","C-06","D-02","D-03","D-04","D-05","D-06","D-07","E-03","E-04","E-05","E-06","E-07","E-08","F-02","F-03","F-04","F-05","F-06","F-07","F-08","G-02","G-03","G-04","G-05","G-06","G-07","H-03","H-04","H-05","H-06","H-07","I-03","I-04","I-05","I-06","I-07","J-04","J-05","J-06"
arcpy.env.workspace=r"F:\data\john_pc2\rogerio\Imagens_Rapid_Eye_Canastra\grass\saidas_area_geral_clip"
for i in range(50):
    query="grade="'\''+lista[i]+'\''
    arcpy.SelectLayerByAttribute_management(grade,"NEW_SELECTION",where_clause=query)
    out=fc[i].replace(".shp","_clip_shp")
    inp=fc[i].replace(".shp",'')
    
    arcpy.Clip_analysis(inp,grade,out)
    arcpy.SelectLayerByAttribute_management(grade,"CLEAR_SELECTION")