#Python Backup Assistant
#Simple program to back up stuff
#Made by Noah Torname

#import stuff
import datetime
import zipfile
import zlib
import os

a = datetime.datetime.now()

#recursive function for nested directories
def zipAll (pth, fil):
    directory = "%s%s%s" % (str(pth), str(fil), "\\")
    for item in blacklist:
        if item == directory:
            print ("\n%s is blacklisted" % directory)
        else:
            if os.path.isdir(directory): #if it is a directory
                print ("\nGoung into %s" % directory)
                for file in os.listdir(directory):
                     zipAll(directory, file)   
            else: #if it is a file
                print ("Compressing:", fil)
                try:
                    archive.write("%s%s" % (pth, fil))
                except:
                    print ("%s%s unsuccesfully written!" % (pth, fil))

#set up destination file path
try:
    file = open('destination.txt', 'r')
    dest = file.read()
    file.close()
    destname = "%s\\%s%s" % (str(dest), str(datetime.date.today()), ".zip")
except:
    text = open("destination.txt", "w")
    text.write("enter the destination file path here, ending with '\\'")
    text.close()
    input ("destination.txt not found! Creating one now. Press any key to exit.")
    quit()

#get sources
try:
    file = open('sources.txt', 'r')
    sources = file.read().splitlines()
    file.close()
except:
    text = open("sources.txt", "w")
    text.write("enter the source file paths here, ending with '\\'")
    text.close()
    input ("sources.txt not found! Creating one now. Press any key to exit.")
    quit()

#get blacklist
try:
    file = open('blacklist.txt', 'r')
    blacklist = file.read().splitlines()
    file.close()
except:
    text = open("blacklist.txt", "w")
    text.write("enter the blacklisted paths here, ending with '\\'")
    text.close()
    input ("blacklist.txt not found! Creating one now. Press any key to exit.")
    quit()

#add to zip archive
archive = zipfile.ZipFile(destname, mode='a', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
for source in sources:
    print ("\nGoing through", source, "...")
    for file in os.listdir(source):
        zipAll(source, file)

b = datetime.datetime.now()
archive.close()

print ("\n\nBackup completed in ", b - a)
print ("The backup is", (int)(os.path.getsize(destname) / 1073741824 * 10 + 0.5)/10, "GB large.")
input ("Press any key to exit.")
