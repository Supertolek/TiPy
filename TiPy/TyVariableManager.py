def getVariableName(variables, variable):
    if variable in variables:
        return variables[variable]["name"]
    else:
        return False

def getVariableType(variables, variable):
    if variable in variables:
        return variables[variable]["type"]
    else:
        return False

def canCreateVariable(variables, variableName, variableType):
    variablesCopy = variables
    if len(variablesCopy["types"][variableType]["used"]) < len(variablesCopy["types"][variableType]["validNames"]):
        if not variableName in ["types", ""]:
            return True
        else:
            return False
    else:
        return False

def createVariable(variables, variableName, variableType):
    variablesCopy = variables
    if len(variablesCopy["types"][variableType]["used"]) < len(variablesCopy["types"][variableType]["validNames"]):
        if not variableName in ["types", ""]:
            variablesCopy[variableName] = {"type": variableType, "name": variablesCopy["types"][variableType]["validNames"][len(variablesCopy["types"][variableType]["used"])]}
            variablesCopy["types"][variableType]["used"].append(variableName)
            return variablesCopy
        else:
            return False
    else:
        return False