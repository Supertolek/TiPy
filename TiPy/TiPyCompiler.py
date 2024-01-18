import tkinter
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import messagebox
# Rich
from rich import print
# TiPy librairies
from TyPrecompile import precompile
from TyCompile import compileCode
from idlelib.percolator import Percolator
from idlelib.colorizer import ColorDelegator

folderPath = "/"
code = ""

textEditor = None
isTextEditorShown = False
textEditorContent = ""

window = tkinter.Tk()
window.title("Ti Python")

def openFile():
	global code
	global folderPath
	global textEditorContent
	print("[bold]Action :[/bold] open")
	filename = filedialog.askopenfilename(title="Open a file", initialdir=folderPath, filetypes=(("Ti Python files", "*.tipy"), ("Text files", "*.txt"), ("All files", "*.*")))
	folderPath = filename[:filename.rindex("/")]
	print("[bold]Folder :[/bold] \"" + folderPath + "\"")
	print("[bold]File   :[/bold] \"" + filename + "\"")
	if filename == "":
		print("⚠️  [red]No file selected[/red]")
	else:
		try:
			code = open(filename, "r").read()
			msg_box = tkinter.messagebox.askyesno("Replace code", "Do you want to replace the actual program?", icon="question")
			print("[bold]Replace:[/bold] " + str(msg_box))
			if msg_box:
				hideTextEditor()
				textEditorContent = code
				showTextEditor()
		except:
			code = ""
			print("⚠️  [red]Unable to read file[/red] \"" + filename + "\"")

def newFile():
	print("[bold]Action :[/bold] new")
	print("⚠️  This is useless.")
	tkinter.messagebox.showwarning(title="Work in progress feature", message="This is useless.")
	showTextEditor()

def saveFile():
	print("[bold]Action :[/bold] save")
	print("⚠️  This is not availlable yet.")
	tkinter.messagebox.showwarning(title="Work in progress feature", message="You cannot save the file now.")
	# saveLocation = asksaveasfile(initialfile="untitled.8xp", defaultextension=".8xp", filetypes=[("Ti Basic", "*.8xp"), ("Text documents", "*.txt"), ("All files", "*.*")])
	# saveLocation.write("\n".join(textEditorContent))
	# saveLocation.close()

def closeFile():
	print("[bold]Action :[/bold] close")
	print("⚠️  This is useless.")
	tkinter.messagebox.showwarning(title="Work in progress feature", message="This is useless.")
	hideTextEditor()

def compileFile():
	global code
	print("[bold]Action :[/bold] compile")
	if code == "":
		print("⚠️ \t [red]Please load a program to compile[/red]")
	else:
		preCompiledCode = precompile(code)
		compiledCode = compileCode(preCompiledCode)
		print("\n".join(compiledCode))
		# Code display
		compiledCodeDisplay = tkinter.Toplevel(window)
		compiledCodeDisplay.title("Code output")
		displayTextWidget = tkinter.Text(compiledCodeDisplay)
		displayTextWidget.insert(tkinter.END, "\n".join(compiledCode))
		displayTextWidget.pack()
		# Menu bar
		def saveCode():
			print("⚠️  Due to strange encoding, you cannot save this file as ti basic program now.")
			tkinter.messagebox.showwarning(title="Work in progress feature", message="You cannot save the file as ti basic now. Try to copy and paste it.")
			# saveLocation = asksaveasfile(initialfile="untitled.8xp", defaultextension=".8xp", filetypes=[("Ti Basic", "*.8xp"), ("Text documents", "*.txt"), ("All files", "*.*")])
			# for line in compiledCode:
			# 	saveLocation.write("\n".join(line))
		displayMenuBar = tkinter.Menu(compiledCodeDisplay)
		saveMenu = tkinter.Menu(displayMenuBar, tearoff=0)
		saveMenu.add_command(label="Save", command=saveCode)
		displayMenuBar.add_cascade(label="Options", menu=saveMenu)
		compiledCodeDisplay.config(menu=saveMenu)

def showTextEditor():
	global isTextEditorShown
	global textEditorContent
	if not isTextEditorShown:
		global textEditor
		textEditor = tkinter.Text(window)
		textEditor.insert(tkinter.END, textEditorContent)
		textEditor.pack()
		Percolator(textEditor).insertfilter(ColorDelegator())
		isTextEditorShown = True

def hideTextEditor():
	global isTextEditorShown
	global textEditorContent
	global code
	if isTextEditorShown:
		global textEditor
		global textEditorContent
		textEditorContent = textEditor.get("1.0", tkinter.END)
		textEditor.destroy()
		isTextEditorShown = False
		code = textEditorContent

# Menu bar
menuBar = tkinter.Menu(window)
filemenu = tkinter.Menu(menuBar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save as...", command=saveFile)
filemenu.add_command(label="Close", command=closeFile)
filemenu.add_separator()
filemenu.add_command(label="Compile", command=compileFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menuBar.add_cascade(label="File", menu=filemenu)
viewmenu = tkinter.Menu(menuBar, tearoff=0)
viewmenu.add_command(label="Show editor", command=showTextEditor)
viewmenu.add_command(label="Hide editor", command=hideTextEditor)
menuBar.add_cascade(label="View", menu=viewmenu)
window.config(menu=menuBar)

window.mainloop()