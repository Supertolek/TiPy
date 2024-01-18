import importlib
from TyPrecompile import precompile

def add(number1, number2):
    return number1 + number2
def substract(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    return number1 / number2
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def optimise(code):
    output = code
    arguments = code["arguments"]
    for argumentIndex, argument in enumerate(arguments):
        if not argument["alone"]:
            if len(argument["content"]) == 3:
                calcul = ["number", "operator", "number"]
                for i, part in enumerate(argument["content"]):
                    if part["type"] != calcul[i]:
                        return(code)
                output["arguments"][argumentIndex] = {"alone": True, "type": "number", "content": operations[argument["content"][1]["content"]](argument["content"][0]["content"], argument["content"][2]["content"])}
    return output

librairies = {}

index = {}

def importStatement(args, variables):
    variablesCopy = variables
    output = ""
    for arg in args:
        if arg["alone"]:
            try:
                librairy = importlib.import_module("TyClass" + str(arg["content"]).capitalize())
                librairies[librairy.name] = librairy
                index[librairy.name] = librairy.index
                init, variablesCopy = index[librairy.name]["_settings"]({}, variables)
                if str(init) != "":
                    output += str(init) + ";"
            except:
                return "", variables
    return output, variablesCopy

index["master"] = {
    "import": importStatement
}

variables = {"types":{
    "number": {
        "validNames": "ABCDEFGHIJKLMNOPQRSTUVWXYZθ",
        "used": []
    }
}}

def compileCode(code, errorSensitive:bool = True):
    global variables
    output = []
    for lineIndex, rawLine in enumerate(code):
        line = optimise(rawLine)
        functionData =  line["function"]
        functionNameSpace = functionData["class"]
        functionName = functionData["function"]
        arguments = line["arguments"]
        if functionNameSpace in index and functionName in index[functionNameSpace]:
            try:
                result = index[functionNameSpace][functionName](arguments, variables)
                variables = result[1]
                if result[0] != "":
                    output.append(result[0])
            except:
                if errorSensitive:
                    return f"Syntax error\nCheck if you gave the right arguments.\nAt line {lineIndex} : {rawLine}"
                else:
                    print(f"Syntax warning\nCheck if you gave the right arguments.\nAt line {lineIndex} : {rawLine}")
        else:
            if errorSensitive:
                return f"Syntax error\nCheck if you spelled right both function name and function namespace.\nIf the error occurs, check if you imported {functionNameSpace}.\nmaster.import({functionNameSpace})"
            else:
                print(f"Syntax error\nCheck if you spelled right both function name and function namespace.\nIf the error occurs, check if you imported {functionNameSpace}.\nmaster.import({functionNameSpace})")
    return output
