import json
class FileReader:

  def read_file(self, path):
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
