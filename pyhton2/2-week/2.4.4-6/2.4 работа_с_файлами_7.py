import os
import os.path
import shutil

#shutil.copy("2.4.4/text1.txt", "2.4.4/text11.txt")
shutil.copytree("2.4.4", "2.4.4/2.4.4")

#print(os.getcwd())
#print(os.listdir(".idea"))

#print(os.path.exists("fib.py"))
#print(os.path.exists("2.4.4"))

#print(os.path.isfile("fib.py"))
#print(os.path.isfile("2.4.4"))

#print(os.path.isdir("fib.py"))
#print(os.path.isdir("2.4.4"))

#print(os.path.abspath("fib.py"))

#os.chdir("2.4.4")
#print(os.getcwd())

for current_dir, dirs, files, in os.walk("."):
    print(current_dir, dirs, files)
