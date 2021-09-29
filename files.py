import os, shutil


files = os.listdir('.')

# print(files)

def manage_files(files, extension):

    files_ext = sort_files_with_extension(files, extension.lower() )

    for i in range(len(files_ext)):
        print("[ " + str(i) +  " ] " + files_ext[i])

    create_dir(extension)

    move_files(files_ext, ".\\" + extension)


def sort_files_with_extension(files, extension):
    result = []
    for f in files:
        if(f.endswith(extension)):
            result.append(f)
    
    return result



def create_dir(name):
    try:
        os.mkdir(os.getcwd() + "\\" + name)
    except:
        print("no se pudo crear el directorio: " + name)


def move_files(files, path):
    for f in files:
        try:
            print("Copying: " + str(f) + " in: " + path)
            shutil.move(f, path)
        except Exception as e:
            print("No se pudo mover: ", str(f) + " porque: " + str(e))
    

manage_files(files, "TORRENT")

