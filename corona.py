import os
import pandas as pd
from helpers.FileReader import FileReader

def __load_dataframe(data):
  df = pd.DataFrame(data, columns=['paper_id', 'title', 'abstract', 'text'])
  print(df.describe(include='all'))

  # Clean Data
  df.drop_duplicates(['abstract'], inplace=True)
  print(df.describe(include='all'))

# Load data
data = FileReader().process()
__load_dataframe(data)