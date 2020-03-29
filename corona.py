import os
import pandas as pd
from tqdm import tqdm
from helpers.FileReader import FileReader

BASE_PATH = 'dataset'
dirs = ['biorxiv_medrxiv']

def iterate_folders(dirs):
  docs = []
  for d in dirs:
    for file in tqdm(os.listdir(f"{BASE_PATH}/{d}/{d}")):
      file_path = f"{BASE_PATH}/{d}/{d}/{file}"
      contents = FileReader().read_file(file_path)
      docs.append(contents)
    return docs
  
data = iterate_folders(dirs)
df = pd.DataFrame(data, columns=['paper_id', 'title', 'abstract', 'text'])
print(df.describe(include='all'))