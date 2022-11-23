import os
from glob import glob
from azure.storage.blob import BlobServiceClient

storage_account_key = "insert your here"
storage_account_name = "insert your here"
connection_string = "insert your here"
container_name = "insert your here"

files = []
allfiles = []


def uploadToBlobStorage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded {file_name}.")


dir = "*"
while True:
    files = glob(f"{dir}")
    if not files:
        break
    for file in files:
        if os.path.isfile(file) and file !=__file__:
            file = file.replace("\\", "/")
            allfiles.append(file)
    dir += "\*"


print(f"Files to upload: {allfiles}")
print("Press Enter to continue...")
input()

for file in allfiles:
    uploadToBlobStorage(file, file)

print("All done.")
input()
