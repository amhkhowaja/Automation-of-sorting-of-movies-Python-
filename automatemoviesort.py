import os
import shutil
import re
#To categorize the movies and sort out with the year name:
sdir=input("Enter the source path:")        #mine was 'F:\movies'
os.chdir(sdir)
files=os.listdir()

for file in files:                          #file is the name of full file
    fnames=re.split("\s|(?<!\d)[,.](?!\d)", file)                 #fnames is the list of filename splited into words
    pathd=os.path.join(sdir, file)              #sdir= 'F:\movies'
    for fname in fnames:
        fname = fname.strip('()')
        if fname.isnumeric():
            year=int(fname)
            
            if year>=2000 and year <=2021:          #sorting all movies which are released between 2000 and 2021
                #print(year)
                if os.path.exists(pathd)==False:
                    os.mkdir(str(year))
                src=os.path.join(sdir, file)
                dsn=os.path.join(sdir, str(year)+"\\")
                print(file,"is being copied in ",str(year),"....." )
                #if os.path.isdir(pathd):
                #os.rename(src,os.path.join(dsn,file))
                shutil.move(src,dsn) 
                
                print(file, "is successfully copied")
                break
print("Processing Finished, Sorting of the Folder has been completed.")
