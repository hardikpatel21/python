import os

def rename_files():
    # (1) get file names from a folder
      file_list = os.listdir(r"/Users/Hardik/Documents/Study/Udacity/Secret_message/greetings")
      print (file_list)
      folder_path = os.getcwd()
      print (folder_path)
      os.chdir(r"/Users/Hardik/Documents/Study/Udacity/Secret_message/greetings")

    #(2) for each file, renme filename

      for file_name in file_list:
          #print ("old file :"+file_name)
          #print ("new file is :" + file_name.translate(None,"0123456789"))
          os.rename(file_name,file_name.translate(None,"0123456789"))

      print "now check your secreat message"
  
rename_files()
    
