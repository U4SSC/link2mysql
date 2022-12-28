import os

if __name__ == "__main__":
    try:
        os.mkdir("./csvupload")
    except:
        print("Folder 'csvupload' already exist !")
    with open('./country_list.json', 'w') as fp:
        pass
    os.system("pip install -r requirements.txt")
    