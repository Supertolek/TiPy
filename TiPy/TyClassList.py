from TyVariableManager import getVariableName, getVariableType, createVariable, canCreateVariable
from TyPunctuation import Punctuation, contains

def init(args, variables):
	variablesCopy = variables
	variablesCopy["types"]["list"] = {"used": [], "validNames": ["L₁", "L₂", "L₃", "L₄", "L₅", "L₆"]}
	return "", variablesCopy

def formatList(args):
	output = []
	if args[0]["content"][0] in Punctuation.listEnter and args[-1]["content"][-1] in Punctuation.listExit:
		firstArgument = args[0]["content"][1:]
		try:
			firstArgument = float(firstArgument)
			output.append(firstArgument)
		except:
			output.append(args[0]["content"][1:])
		for arg in range(len(args)-2):
			if type(args[arg+1]["content"]) == str and args[arg+1]["content"][-1] in Punctuation.listExit:
				return output
			else:
				output.append(args[arg+1]["content"])
		lastArgument = args[-1]["content"][0:-1]
		try:
			lastArgument = float(lastArgument)
			output.append(lastArgument)
		except:
			output.append(args[-1]["content"][0:-1])
	return output

# Variables
def setStatement(args, variables):
	variablesCopy = variables
	output = ""
	if len(args) > 2:
		output += "{"
		formatedList = formatList(args[1:])
		for item in formatedList:
			output += str(item)
			output += ","
		output = output[0:-1]
		output += "}"
	elif args[1]["type"] == "variable":
		output += args[1]["content"]
	output += "→"
	listType = getVariableType(variablesCopy, args[0]["content"])
	if listType and listType == "list":
		output += getVariableName(variablesCopy, args[0]["content"])
	elif canCreateVariable(variablesCopy, args[0]["content"], "list"):
		variablesCopy = createVariable(variablesCopy, args[0]["content"], "list")
		output += getVariableName(variablesCopy, args[0]["content"])
	return output, variablesCopy

name = "list"

index = {
	"_settings": init,
	"set": setStatement
}