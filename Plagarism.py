import sys
import re
import os
from tkinter import filedialog
from tkinter.ttk import * 
from tkinter import * 
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

def booyerMoore(directory, text1):
    if os.path.isdir(directory) == 0:
        print("The directory does not exist")
        w3 = Label(app, text="The directory Does not exist")
        w3.pack()
        sys.exit(0)
    for textfile in os.listdir(directory):
        if textfile[0] == "." :
            continue

        print("Checking ",textfile)
        w4 = Label(app,fg = "#FF33D4",
		 
		 font = "Helvetica 16 bold italic",text="Checking "+textfile)
        w4.pack()


        text2 = open(os.path.join(directory,textfile)).read()
        pattern_file    = ''.join(open(text1).readlines())

        sentences = re.split(r'[\.\?!]', pattern_file)
        countermatched = 0
        countertotal = 0

        for pat in sentences:
            pat = pat.strip()

            if len(pat) > 0:
                countertotal += 1
                patternstartpos = 0
                found = 0

                while patternstartpos + len(pat) <= len(text2):

                    j = patternstartpos + len(pat)

                    for i in range(0, len(pat))[::-1]:


                        if pat[i].lower() == text2[j - 1].lower():
                            j = j - 1

                            if j == patternstartpos:
                                found = 1
                                break
                            else:
                                continue


                        else:


                            if pat[0:i].rfind(text2[j - 1]) == -1:
                                patternstartpos = patternstartpos + len(pat)
                                break


                            else:
                                patternstartpos = patternstartpos + len(pat) - pat[0:i].rfind(text2[j - 1]) - 1
                                break


                    if found == 1:  
                        countermatched = countermatched + 1
                        break

        print("Match percentage = %s%%" % (countermatched * 100 / countertotal))
        w = Label(app,  fg = "#3349FF",font = "Helvetica 16 bold italic",text ="Match percentage = %s%%" % (countermatched * 100 / countertotal))
        w.pack()

        if (countermatched * 100 / countertotal) >= 70:
            print("The input file is appears to be plagiarised. %s%% of its content matches with the file %s." % (
            (countermatched * 100 / countertotal), textfile))
            w1 = Label(app,  fg = "#FF335E",
		
		 font = "Helvetica 16 bold italic",text ="The input file is appears to be plagiarised. %s%% of its content matches with the file %s." % (
            (countermatched * 100 / countertotal), textfile))
            w1.pack()
    # return "Match percentage = %s%%" % (countermatched * 100 / countertotal)


# directory = input(" Enter the directory")
# text1 = input (" Enter the text")
# booyerMoore(directory, text1)
directory ="Hello"
text1 ="hellp"
per = 1
app =  Tk()

app.title("Plagarism Detection")
app.geometry('800x600')
# app.configure(bg='red')
app.configure(bg='#C8F9C4')

w = Label(app,  font = "Verdana 16 bold",fg= "light blue",bg= "#6E33FF",text="Plagarism Detection using booyer moore Algorithm")
w.pack()
def folder():
    global directory    
    directory = askdirectory(parent=app,title='Choose directoryectory with image sequence stack files')
    print(directory)
def file():  
    global text1   
    text1 = filedialog.askopenfilename()
    print(text1)
def call():
    global per
    per = booyerMoore(directory,text1)
def quit():
    app.destroy()

btn1 = Button(app, width=15, height=2,text = 'Select input Folder',command = folder,relief=RAISED, bg= '#33FF36') 
btn1.pack()
btn2 = Button(app, width=15, height=2,text = 'Select Pattern File',command = file,relief=RAISED, bg= '#33FF36') 
btn2.pack()
btn3 = Button(app, width=15, height=2,text = 'Check',command = call,relief=RAISED, bg= '#33FF36') 
btn3.pack()
btn3 = Button(app, width=15, height=2,text = 'Quit',command = quit,relief=RAISED, bg= '#33FF36') 
btn3.pack()
# B.place(bordermode=OUTSIDE, height=100, width=100)

# w = Label(app,  text ="Match percentage = %s%%" % (countermatched * 100 / countertotal))
# per = "hello"
print(directory)
print(text1)

# print(directory)
app.mainloop()


