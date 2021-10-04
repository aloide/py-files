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
    

def manage_folder():
    for folder in files:
        filename, extension = os.path.splitext(folder)
        if not extension:
            print(filename)

def list_extensions():
    for f in files:
        extension = os.path.splitext(f)[1]
        if(extension):
            print(extension[1:])
            #print(extension)

def count_files():
    count = 0
    for f in files:
        filename, extension = os.path.splitext(f)
        if(filename and extension) and f != "files.py":
            print(f)
            count +=1
    return count

#manage_files(files, "TORRENT")
#list_extensions()

def main():
    print("Managing your files...")
    n_files = count_files()
    print(n_files, " files finds to manage")
    print("first.. making ", n_files," folders")
    
    

if __name__ == "__main__":
    main()

#manage_folder()




