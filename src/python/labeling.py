from os import listdir
from os.path import isfile, join
import xmltodict
path = "/Users/pal/study/Intro_To_Ml/final_project/final-project-pal0064/data/raw/formsA-D"

form_files = [f for f in listdir(path) if isfile(join(path, f))]
file_name = 'a01-000u.png'


line_path="/Users/pal/study/Intro_To_Ml/final_project/final-project-pal0064/data/processed/lines.txt"
line_list = []

words = open(line_path, "r").readlines()
for line in words:
    if line[0] == "#":
        continue
    line_list.append(line)


path = "/Users/pal/study/Intro_To_Ml/final_project/final-project-pal0064/data/raw/xml"
xml_files = [path+"/"+f for f in listdir(path) if isfile(join(path, f))]

def read(file):
    with open(file) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    return  data_dict

xml_dict = {}
for file in xml_files:
    try:
        text = []
        data = read(file)
        for record in data['form']['machine-printed-part']['machine-print-line']:
            text.append(record['@text'])
        xml_dict[file.split('/')[-1]] = text
    except Exception as e:
        print(e)
        print(file)


import pandas as pd
final_labels = {}
for line in  line_list:
    img_name = line.split(' ')[0]
    form_image_name = "-".join(img_name.split('-')[0:2])
    line_text = " ".join(" ".join(line.split(' ')[8:]).split('|'))
    data = {
        'complete text':line_text,
        'lines': [line_text],
        'line_images':[img_name]
    }
    if final_labels.get(form_image_name):
        final_labels[form_image_name]['complete text'] = final_labels[form_image_name]['complete text']+"\n"+ line_text
        final_labels[form_image_name]['lines'].append(line_text)
        final_labels[form_image_name]['line_images'].append(img_name)
    else:
        final_labels[form_image_name]  = data

records = {
    'form_image':[],
    'complete text':[],
    'lines': [],
    'line_images':[]
}    
for key in final_labels:
    records['form_image'].append(key)
    records['complete text'].append(final_labels[key]['complete text'])
    records['lines'].append(final_labels[key]['lines'])
    records['line_images'].append(final_labels[key]['line_images'])


df = pd.DataFrame(records)

df.to_csv('form_labels.csv',index=False)


    


