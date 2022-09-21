import os

root = 'G:\My Drive\PhD\literature\jabrefLibrary\prio2'
folders = list(os.walk(root))[1:]

for folder in folders:
    # folder example: ('FOLDER/3', [], ['file'])
    if not folder[2]:
        os.rmdir(folder[0])
