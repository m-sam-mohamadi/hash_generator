import hashlib
from progress.bar import Bar
try:
    filename = input("Enter the file you want to hash :D ")
    lowMem = input("Do you want to use low memory mode?[y/N]")
    if filename == "":
        print("Please fill in the file name.")
    hashFile = open("./hashed_output.csv", "w")
    
    if lowMem =="y":
        print("===== Optimizing memory mode :) =====")
        with open(f"./{filename}") as file:
            print("Reading file content...")

            with Bar("Converting...", max=len(file.readlines())) as bar:
                        file.seek(0)
                        for line in file:
                            myHash = hashlib.sha256()
                            ch = bytes(line.strip(), encoding="utf-8")
                            myHash.update(ch)
                            myHash.digest()
                            hashFile.write(line.strip() + "," + myHash.hexdigest() + "\n")
                            bar.next()
        hashFile.close()
        print("Finished.")
    else:
        print("===== Fast converting mode ^_^ =====")
        with open(f"./{filename}") as file:
            print("Reading file content...")
            lines = file.readlines()
            with Bar("Converting...", max=len(lines)) as bar:
                for i in lines:
                    myHash = hashlib.sha256()
                    ch= bytes(f"{i.strip()}",encoding="utf-8") 
                    myHash.update(ch)
                    myHash.digest()
                    hashFile.write(str(i).strip()+","+myHash.hexdigest()+"\n")
                    bar.next()
        hashFile.close()
        print("Finished.")
except FileNotFoundError:
    print("Error: File not found.")


