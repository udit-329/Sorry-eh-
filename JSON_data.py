import json

def data_import(link):
    with open(link, "r") as read_file:
        data = json.load(read_file)
    return data

def data_export(link, data):
    with open(link, "w") as write_file:
        json.dump(data, write_file, indent = "\t")


