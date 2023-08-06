import os
import time
from hashlib import sha256

class DupliCleaner:
    """cleaner class"""
    def __init__(self):
        """Function to get dir"""
        self.home_dir = os.getcwd(); self.File_hashes = []
        self.Cleaned_dirs = []; self.Total_bytes_saved = 0
        self.block_size = 65536; self.count_cleaned = 0

    def welcome_msg(self) -> None:
        """Function to generate an appealing welcome prompt."""
        print("********************************************")
        print("************* DupliCleaner ****************")
        print("********************************************\n\n")
        print("---------------- WELCOME -------------------")
        time.sleep(3)
        print("\n Cleaning ..................................")

    def hash_generator(self, file_name:str) ->str:
        """Function to generate hashes."""
        file_hash = sha256()
        try:
            with open(file_name, "rb") as File:
                file_block = File.read(self.block_size)
                while len(file_block)>0:
                    file_hash.update(file_block)
                    file_block = File.read(self.block_size)
                file_hash = file_hash.hexdigest()
            return file_hash
        except:
            return False

    def rm_files(self) ->None:
        all_dirs = [path[0] for path in os.walk(".")]
        for path in all_dirs:
            os.chdir(path)
            all_files = [file for file in os.listdir() if os.path.isfile(file)]
            for file in all_files:
                fileHash = self.hash_generator(file)
                if not fileHash in self.File_hashes:
                    if fileHash:
                        self.File_hashes.append(fileHash)
                        #print(file)
                    else:
                        byte_saved = os.path.getsize(file)
                        self.count_cleaned += 1
                        self.Total_bytes_saved += byte_saved
                        os.remove(file)
                        filename = file.split("/")[-1]
                        print(filename, ".. cleaned ")
                        os.chdir(self.home_dir)

    def main(self) ->None:
        """Main function of the app"""
        self.welcome_msg()

if __name__ == "__main__":
    App = DupliCleaner()
    App.main()
