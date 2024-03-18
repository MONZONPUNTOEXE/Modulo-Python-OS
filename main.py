import os

# Ir a la dirección deseada, donde tenemos nuestros archivos
os.chdir('C:/.../.../Cambiar nombre de forma masiva/archivos')

# Para saber en que dirección estamos "os.getcwd()"
# print(os.getcwd())

numero = 0
# Recorremos los archivos que tenemos en el directorio
for i in os.listdir():
    # Con esta funcion Separamos el texto de las extenciones
    texto, extension = os.path.splitext(i)
    # Eliminamos la letra que no queramos separando en terminos
    clase, numeroDeClase, materia, materiaDos = texto.split('_')
    
    # Para remplazar un archivo podemos usar "replace('')"
    
    # Creamos los archivos y acraramos que partes queremos que tenga nuestros archivos
    # Como queremos que se modifique el numero hacemos el contador
    numero += 1
    nuevo_archivo = f"{clase}_{numero}_{materia}{extension}"
    print(i)
    # print(nuevo_archivo)
    
    # Para que se guarden los cambios ejecutamos el codigo el siguiente codigo:
    os.rename(i,nuevo_archivo)