import subprocess
import sys
# importing Image class from PIL package 
from PIL import Image


#create the thumbnails subfolder
try:
    retcode = subprocess.call("mkdir" + " thumbnails", shell=True)
    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Thumbnails folder created with return code", retcode, file=sys.stderr)
except OSError as e:
    print("Execution failed:", e, file=sys.stderr)

#get all the files in the folder
output = subprocess.check_output("ls *.jpg", shell=True)

datalist = list(output.decode("utf-8").split()) 
datacount = len(datalist)


#file to generate
file_to_write = open("index.html","w")
#add html values to the generated file
str1 = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Image Gallery</title> \
    <meta name="description" content="Responsive Image Gallery"><meta name="author" content="Konstantinos Sarmidis"><style type="text/css"> \
    </style><link rel="stylesheet" href="styles.css"></head><body><div id="gallery">'

str2 = '</div></body></html>'

#write the header to the file
file_to_write.write(str1)


for i in datalist:
    # creating an image object 
    image = Image.open(i, mode='r')
    MAX_SIZE = (500, 500)
    image.thumbnail(MAX_SIZE)
    
    # creating thumbnail
    image.save("./thumbnails/"+i)
    print("created thumbnail", i,"\\", datacount)

    #write html into the file
    file_to_write.write('<a href ='+i+ '><img src="thumbnails/'+i  +'"></a>\n')
    # image.show() 

#write the footer
file_to_write.write(str2)    
file_to_write.close()

print("procedure completed")