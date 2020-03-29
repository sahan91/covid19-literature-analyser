import json
from tqdm import tqdm
import os
import glob

BASE_PATH = 'dataset'
all_json = glob.glob(f'{BASE_PATH}/biorxiv_medrxiv/**/*.json', recursive=True) # debugging
# all_json = glob.glob(f'{BASE_PATH}/**/*.json', recursive=True)
print(all_json)

class FileReader:

  def process(self):
    return self.__iterate_folders();

  def __read_file(self, path):
    docs = []
    j = json.load(open(path, "rb"))

    # Get Paper ID
    paper_id = j['paper_id']

    # Get Paper Title
    title = j['metadata']['title']

    # Process Abstracts
    try:
      abstract = j['abstract'][0]['text']
    except:
      abstract = ""

    # Process Body Text
    full_text = ""
    for text in j['body_text']:
      full_text += f"{text['text']}\n"

    return [paper_id, title, abstract, full_text]
  
  def __iterate_folders(self):
    docs = []
    for file in tqdm(all_json):
      contents = self.__read_file(file)
      docs.append(contents)
    return docs