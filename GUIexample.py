import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
	with open("save.txt", 'r') as f:
		tempApps = f.read()
		apps = tempApps.split(",")
		apps = [x for x in tempApps if x.strip()]

#Adding an app to be run
def addApp():

	for widget in frame.winfo_children():
		widget.destroy()

	filename= filedialog.askopenfilename(initialdir="/", title="Select File",
		filetypes=(("executables", "*.exe"), ("all files", "*.*")))

	apps.append(filename)
	print(filename)
	for app in apps:
		label = tk.Label(frame, text=app, bg="gray")
		label.pack()

#Loops through apps to run them
def runApps():
	for app in apps:
		os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#ff0080")
canvas.pack()

frame = tk.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text="Open File", padx = 10,
	pady=5, fg='white', bg="#ff0080", command=addApp)

runApps = tk.Button(root, text="Run Apps", padx = 10,
	pady=5, fg='white', bg="#ff0080", command=runApps)

openFile.pack()
runApps.pack()


for app in apps:
	label = tk.Label(frame, text=app)
	label.pack()


root.mainloop()

'''Generate file when you open it up so it "keeps" the files you had previously,
this is done by calling the function that pushes the apps in the list declaration above'''

with open('save.txt', 'w') as f:
	for app in apps:
		f.write(app+',')



