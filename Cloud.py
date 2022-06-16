import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BJoeuh0N4bmS4P0IrSx38l1q7jR6qEaepLsk9HwtmPOTSfJFR0lxjB7P__aofzWvwsFXYsM5idjHT3TvSc9NKKgicoXCdK_EQFgPp45JLgoW-GY5hX07MWuFQFE55bKg38lLmN8'
    transferData = TransferData(access_token)

    file_from=input("enter the file path to tansfer: ")
    file_to=input("enter the full path to upload to dropbox")

    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()    

          


    