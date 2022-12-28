import os

if __name__ == "__main__":
    os.mkdir("./csvupload")
    with open('./country_list.json', 'w') as fp:
        pass
    os.system("pip install -r requirements,txt")
    