from TyPunctuation import Punctuation, contains

def splitArguments(arguments:str) -> dict:
	"""Split the text for each arguments
	Exemple :
	variable "string" 1
	[{"type": "raw", "content": "variable"}, {"type": "string", "content": "string"}, {"type: "raw", "content": "1"}]"""

	isInString = False # Is registering a string (if True, ignore ",")
	isInFunction = False
	functionHeight = 0
	argument = ""
	output = []
	for i, letter in enumerate(arguments):
		if isInFunction:
			if not letter in Punctuation.functionExit:
				argument += letter
			else:
				argument += letter
				functionHeight -= 1
				if functionHeight == 0:
					isInFunction = False
					output.append(argument)
					argument = ""
		else:
			if isInString:
				if letter in Punctuation.stringDelimiter:
					argument += letter
					output.append(argument)
					argument = ""
					isInString = False
				else:
					argument += letter
			else:
				if letter in Punctuation.argumentsDelimiter:
					if argument != "":
						output.append(argument)
						argument = ""
				elif i == len(arguments) - 1:
					argument += letter
					output.append(argument)
					argument = ""
				elif letter in Punctuation.stringDelimiter:
					isInString = True
					argument += letter
				elif letter in Punctuation.functionEnter:
					isInFunction = True
					functionHeight += 1
					argument += letter
				elif letter == " ":
					argument += letter
				else:
					argument += letter
	return output

def extractArguments(arguments:list) -> list:
	"""
	transform list into dict:
	[{"alone": True, "type": "string", "content": "string"}, {"alone": False, "content": [{"type": "variable", "content": "variable"}, {"type": "operator", "content": "+"}, {"type": "int", "content": 10}]}]"""
	output = []
	for argument in arguments:
		isInString = False
		isInFunction = False
		functionHeight = 0
		functions = []
		isInKey = False
		key = ""
		keys = []
		for letter in argument:
			if isInFunction:
				# This part is executed when in a function
				if letter in Punctuation.functionExit:
					functionHeight -= 1
					if functionHeight == 0:
						functionContent = precompileLine(key)
						keys.append({"type": "function", "content": functionContent})
						key = ""
						isInFunction = False
						isInKey = False
				else:
					key += letter
			else:
				if isInString:
					# This part is executed when in string
					if letter in Punctuation.stringDelimiter:
						key += letter
						keys.append({"type": "string", "content": key})
						key = ""
						isInString = False
						isInKey = False
					else:
						key += letter
				else:
					# This part is executed when not in string or function
					# Detect if we enter in string or functino
					if letter in Punctuation.stringDelimiter:
						# Detect if already in a key, if so save the key
						if isInKey:
							try:
								float(key)
								keys.append({"type": "number", "content": float(key)})
							except:
								keys.append({"type": "variable", "content": key})
						key += letter
						isInString = True
					elif letter in Punctuation.functionEnter:
						# Detect if already in a key, if so save the key
						if isInKey:
							try:
								float(key)
								keys.append({"type": "number", "content": float(key)})
							except:
								keys.append({"type": "variable", "content": key})
							key = ""
						functionHeight += 1
						isInFunction = True
						isInKey = True
					elif letter in Punctuation.operators:
						if isInKey:
							try:
								float(key)
								keys.append({"type": "number", "content": float(key)})
							except:
								keys.append({"type": "variable", "content": key})
							key = ""
							isInKey = False
						keys.append({"type": "operation", "content": letter})
					elif isInKey:
						# Detect if already in a key
						if letter == " ":
							try:
								float(key)
								keys.append({"type": "number", "content": float(key)})
							except:
								keys.append({"type": "variable", "content": key})
							key = ""
							isInKey = False
						else:
							key += letter
					else:
						# Otherwise enter in key mode if not a space
						if letter != " ":
							key += letter
							isInKey = True
		#  Check a last time to save the last item
		if isInFunction:
			functionContent = precompileLine(key)
			keys.append({"type": "function", "content": functionContent})
		elif isInString:
			keys.append({"type": "string", "content": key})
		elif isInKey:
			try:
				float(key)
				keys.append({"type": "number", "content": float(key)})
			except:
				keys.append({"type": "variable", "content": key})
		if len(keys) == 1:
			output.append({"alone": True, "type": keys[0]["type"], "content": keys[0]["content"]})
		else:
			output.append({"alone": False, "content": keys})
	return output

def extractFunction(code):
	functionName = ""
	index = -1
	for i, letter in enumerate(code):
		if letter in Punctuation.functionContentEnter:
			index = i
			break
		functionName += letter
	if index != -1:
		if contains(functionName, Punctuation.classChildren):
			functionNameSplited = functionName.split(".")
		else:
			functionNameSplited = ["main", functionName]
		return {"class": functionNameSplited[0], "function": functionNameSplited[1]}, index
	else:
		return False

def precompileLine(rawCode):
	for i in range(len(rawCode)):
		if not rawCode[i] in [" ", "	"]:
			code = rawCode[i : len(rawCode)]
			break
	if not code[0] in Punctuation.singleLineComment:
		functionDict, functionEnd = extractFunction(code)
		argumentsToInterpret = splitArguments(code[functionEnd + 1 : -1])
		arguments = extractArguments(argumentsToInterpret)
		return {"function": functionDict, "arguments": arguments}

def precompile(rawCode):
	code = "master.import(main);" + rawCode
	splitedCode = []
	line = ""
	isInString = False
	isInComment = False
	isInList = False
	listLevel = 0
	for letter in code:
		if isInString:
			if letter in Punctuation.stringDelimiter:
				isInString = False
		elif isInComment:
			if letter in Punctuation.singleLineComment:
				isInComment = False
		else:
			if letter in Punctuation.stringDelimiter:
				isInString = True
			elif letter in Punctuation.singleLineComment:
				isInComment = True
			elif letter == ";":
				splitedCode.append(line)
				line = ""
		if not letter in [";", "\n", "\t"]:
			line += letter
	if line != "":
		splitedCode.append(line)
		print("Warning : Did you forgot to add a coma?")
	formatedCode = []
	for codeLine in splitedCode:
		formatedCode.append(precompileLine(codeLine))
	return formatedCode
