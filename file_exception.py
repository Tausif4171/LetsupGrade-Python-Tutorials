import os
import io
if not os.path.exists("abc.txt"):
  with open("abc.txt", 'w') as file:
      file.write(" This is a demo file created")
      print("File created")
else:
  print("File present now")
try:
  with open("demo.txt",'r') as file:
      file.write("Hello everyone")
except FileNotFoundError as fileError:
    print("File not present please create the file" + str(fileError))
except io.UnsupportedOperation as error:
    print("File error: " +str(error))
    
    