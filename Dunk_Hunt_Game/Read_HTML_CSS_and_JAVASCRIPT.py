import webbrowser
import codecs
f = open('Title-screen.html', 'r')
print(f)
file1 = codecs.open("Title-screen.html", 'r', "utf-8")
file2 = codecs.open("Title-screen.css",'r', "utf-8")
file3 = codecs.open("Dog_move.html", 'r', "utf-8")
file4 = codecs.open("Dog_move.css", 'r', "utf-8")
file5 = codecs.open("dog_Hide_and_Jump.html", 'r', "utf-8")
file6 = codecs.open("dog_Hide_and_Jump.css", 'r', "utf-8")
file7 = codecs.open("Giri_Game.html", 'r', "utf-8")
file8 = codecs.open("Game.css",'r', "utf-8")
print(file1.read())
print(file2.read())
print(file3.read())
print(file4.read())
print(file5.read())
print(file6.read())
print(file7.read())
print(file8.read())
webbrowser.open_new_tab('Title-screen.html')
f.close()




