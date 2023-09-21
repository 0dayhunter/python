from zipfile import ZipFile
import os

source_dir = "ITLAB10"
zip_file_name = "sampleDir.zip"

with ZipFile(zip_file_name, 'w') as zipObj:
    for folderName, subfolders, filenames in os.walk(source_dir):
        for filename in filenames:
            filePath = os.path.join(folderName, filename)
            zipObj.write(filePath, os.path.relpath(filePath, source_dir))
