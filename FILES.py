import os
import shutil

def clean_cache():
    path = os.getcwd()
    if not os.path.exists("cache"):
        os.makedirs("cache")
    else:
        shutil.rmtree("cache")
    os.makedirs("cache")


#bron:codegrepper.com (aangepast met hulp docent Winc)
from functools import cache
import os
import shutil

def clean_cache():
    if os.path.exists(".\\files\\cache"):
        shutil.rmtree(".\\files\\cache")
        os.mkdir(".\\files\\cache")
    if not os.path.exists(".\\files\\cache"):
        os.mkdir(".\\files\\cache")
    
        
#bron:thispointer.com
from zipfile import ZipFile

def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path,'r') as zipObj:
        zipObj.extractall(cache_dir_path)
my_zip_file = './files/data.zip'
my_cache_dir = './files/cache/'
cache_zip(zip_file_path = my_zip_file, cache_dir_path = my_cache_dir)

#bron:pythonpool.com (aangepast met hulp docent Winc)
import pathlib
def cached_files():
    path = os.path.join(os.getcwd(), "files", "cache")
    list_files_in_cache = []
    for file in os.listdir(path):
        list_files_in_cache.append(os.path.abspath(os.path.join(path, file)))
    return list_files_in_cache


def find_password(list_files_in_cache): 
    for password in list_files_in_cache:
        with open(password, 'r') as f:            
            text = f.readlines()
            for password in text:
                if 'password' in password:
                    return password[10:-1]                  
