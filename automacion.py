import shutil
 
# archivo de fuente
fuente = "/.../archivo1.txt"
 
# destinación
destino = "/.../archivo1.txt"
 
shutil.copy(fuente, destino)
print("Archivo copiado.")

#########################################

# empleando try..except
try:
    shutil.copy(fuente, destino)
    print("File copied successfully.")
 
# If source and destination are same
except shutil.SameFileError:
    print("Source and destination represents the same file.")
 
# If there is any permission issue
except PermissionError:
    print("Permission denied.")
 
# For other errors
except:
    print("Error occurred while copying file.")
