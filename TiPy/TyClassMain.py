from TyVariableManager import getVariableName, getVariableType, createVariable, canCreateVariable

def init(args, variables):
	return "", variables

# Controls
def ifStatement(args, variables):
	variablesCopy = variables
	output = "If "
	for i, arg in enumerate(args):
		if arg["alone"]:
			if part["type"] == "variables":
				if getVariableName(part["content"]):
					output += variablesCopy[part["content"]]["name"]
				else:
					if createVariable(variables, "nothing!", "number"):
						variablesCopy = createVariable(variables, part["content"], "number")
					else:
						return "", variables
			else:
				output += str(part["content"])
		else:
			for part in arg["content"]:
				if part["type"] == "variables":
					if getVariableName(part["content"]):
						output += variablesCopy[part["content"]]["name"]
					else:
						if createVariable(variables, "nothing!", "number"):
							variablesCopy = createVariable(variables, part["content"], "number")
						else:
							return "", variables
				else:
					output += str(part["content"])
		if i < len(args) - 1:
			output += " et "
	output += ":Then"
	return output, variablesCopy
def elifStatement(args, variables):
	variablesCopy = variables
	output = "If "
	for i, arg in enumerate(args):
		if arg["alone"]:
			if part["type"] == "variables":
				if getVariableName(part["content"]):
					output += variablesCopy[part["content"]]["name"]
				else:
					if createVariable(variables, "nothing!", "number"):
						variablesCopy = createVariable(variables, part["content"], "number")
					else:
						return "", variables
			else:
				output += str(part["content"])
		else:
			for part in arg["content"]:
				if part["type"] == "variables":
					if getVariableName(part["content"]):
						output += variablesCopy[part["content"]]["name"]
					else:
						if createVariable(variables, "nothing!", "number"):
							variablesCopy = createVariable(variables, part["content"], "number")
						else:
							return "", variables
				else:
					output += str(part["content"])
		if i < len(args) - 1:
			output += " et "
	output += ":Then"
	return output, variablesCopy
def elseStatement(args, variables):
	return "Else", variables
def forStatement(args, variables):
	variablesCopy = variables
	output = "For("
	argsTypes = ["variable", "number", "number", "number"]
	for i in range(len(args)):
		if args[i]["alone"]:
			if args[i]["type"] == argsTypes[i]:
				if args[i]["type"] == "variable":
					if getVariableName(variablesCopy, args[i]["content"]) and getVariableType(variablesCopy, args[i]["content"]) == "number":
						output += getVariableName(args[i]["content"])
					else:
						if canCreateVariable(variablesCopy, args[i]["content"], "number"):
							variablesCopy = createVariable(variablesCopy, args[i]["content"], "number")
							output += getVariableName(variablesCopy, args[i]["content"])
						else:
							return "", variables
				else:
					output += str(args[i]["content"])
			if i < len(args) - 1:
				output += ","
		else:
			return "", variables
	output += ")"
	return output, variablesCopy
def endStatement(args, variables):
	return "End", variables
def whileStatement(args, variables):
	variablesCopy = variables
	output = "While "
	for i, arg in enumerate(args):
		if arg["alone"]:
			if arg["type"] == "variables":
				if getVariableName(arg["content"]):
					output += variablesCopy[arg["content"]]["name"]
				else:
					if createVariable(variables, "nothing!", "number"):
						variablesCopy = createVariable(variables, arg["content"], "number")
					else:
						return "", variables
			else:
				output += str(arg["content"])
		else:
			for part in arg["content"]:
				if part["type"] == "variables":
					if getVariableName(part["content"]):
						output += variablesCopy[part["content"]]["name"]
					else:
						if createVariable(variables, "nothing!", "number"):
							variablesCopy = createVariable(variables, part["content"], "number")
						else:
							return "", variables
				else:
					output += str(part["content"])
		if i < len(args) - 1:
			output += " et "
	return output, variablesCopy

# Output
def printStatement(args, variables):
	variablesCopy = variables
	output = "Disp "
	for arg in args:
		if arg["alone"]:
			if arg["type"] == "variable":
				if getVariableName(variablesCopy, arg["content"]):
					output += variablesCopy[arg["content"]]["name"]
				else:
					if canCreateVariable(variables, "nothing", "number"):
						variablesCopy = createVariable(variables, arg["content"], "number")
						output += getVariableName(variablesCopy, arg["content"])
					else:
						return "", variables
			else:
				output += str(arg["content"])
		else:
			for part in arg["content"]:
				if part["alone"]:
					if part["type"] == "variables":
						if getVariableName(part["content"]):
							output += variablesCopy[part["content"]]["name"]
						else:
							if createVariable(variables, "nothing!", "number"):
								variablesCopy = createVariable(variables, part["content"], "number")
								output += variablesCopy[part["content"]]["name"]
							else:
								return "", variables
					else:
						output += str(part["content"])
		output += ","
	return output.removesuffix(","), variablesCopy

# Variables
def setStatement(args, variables):
	variablesCopy = variables
	output = ""
	if len(args) == 2:
		if args[1]["alone"] and args[1]["type"] in ["number", "function"]:
			output += str(args[1]["content"])
		elif args[1]["alone"] and args[1]["type"] == "variable":
			if getVariableName(variablesCopy, args[1]["content"]):
				output += variablesCopy[args[1]["content"]]["name"]
			else:
				if canCreateVariable(variables, "nothing", "number"):
					variablesCopy = createVariable(variables, args[1]["content"], "number")
					output += getVariableName(variablesCopy, args[1]["content"])
				else:
					return "", variables
		else:
			return "", variables
		output += "→"
		if args[0]["alone"] and args[0]["type"] == "variable":
			if getVariableName(variablesCopy, args[0]["content"]):
				output += variablesCopy[args[0]["content"]]["name"]
			else:
				if canCreateVariable(variables, "nothing", "number"):
					variablesCopy = createVariable(variables, args[0]["content"], "number")
					output += getVariableName(variablesCopy, args[0]["content"])
				else:
					return "", variables
		else:
			return "", variables
	else:
		return "", variables
	return output, variablesCopy
def incrementStatement(args, variables):
	variablesCopy = variables
	output = ""
	if len(args) == 2:
		if args[0]["type"] == "variable" and args[1]["type"] == "number":
			if getVariableName(variablesCopy, args[0]["content"]):
				variableName = variablesCopy[args[0]["content"]]["name"]
			else:
				if canCreateVariable(variables, "nothing", "number"):
					variablesCopy = createVariable(variables, args[0]["content"], "number")
					variableName = getVariableName(variablesCopy, args[0]["content"])
				else:
					return "", variables
			output += variableName + "+" + str(args[1]["content"]) + "→" + variableName
	elif len(args) == 1:
		if getVariableName(variablesCopy, args[0]["content"]):
			variableName = variablesCopy[args[0]["content"]]["name"]
		else:
			if canCreateVariable(variables, "nothing", "number"):
				variablesCopy = createVariable(variables, args[0]["content"], "number")
				variableName = getVariableName(variablesCopy, args[0]["content"])
			else:
				return "", variables
		output += variableName + "+1" + "→" + variableName
	else:
		return "", variables
	return output, variablesCopy

name = "main"

index = {
	"_settings": init,
	"if": ifStatement,
	"elif": elifStatement,
	"else": elseStatement,
	"for": forStatement,
	"while": whileStatement,
	"end": endStatement,
	"print": printStatement,
	"set": setStatement,
	"increment": incrementStatement
}