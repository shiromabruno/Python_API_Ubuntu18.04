from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/calculator/requestparam')
def do_calc_param():

    operation = str(request.args.get("operation"))
    value1 = str(request.args.get("value1"))
    value2 = str(request.args.get("value2"))

    validator = checkParam(operation, value1, value2)

    if validator == False:
        retorno_error = {
            "Message: " : "Preencha todos os campos da URL: operation, value1 e value2"
        }
        return retorno_error, 400

    validator = checkData(operation, value1, value2)

    if validator == False:
        retorno_error={
            "Message: " : "Valores incorretos, precisa ser numerios value1 e value2. Ou se divisao, value2 nao pode ser 0"
        }
        return retorno_error, 400

    value1 = int(request.args.get("value1"))
    value2 = int(request.args.get("value2"))
    
    #match  operation: case "sum": somente PYTHON 3.10
    if operation == "sum":
            result = value1 + value2
    elif operation == "minus":
            result = value1 - value2
    elif operation == "multi":
            result = value1 * value2
    elif operation == "div":
            result = value1 / value2
    else:
         operation = "none"

    if operation == "none":
        retornoJson ={
         "resultado" : "operacao invalida",
         "Operation/Value1/Value2": [operation,value1,value2],
         "ExecOK?": False,
         "TypeRequisition": "Parameter"
        }
        return retornoJson, 400
    else: 
        resultstring = str(result)
        
        arrayofobject = [
        {
            "operation": operation,
            "value1": value1
        },
        {
            "operation": operation,
            "value2": value2
        }
        ]

        retornoJson ={
         "resultado" : resultstring,
         "Operation/Value1/Value2/ArrayOfObject": [operation,value1,value2, arrayofobject],
         "ExecOK?": True,
         "TypeRequisition": "Parameter"
        }
    #return "2 + 2 eh: " + calculostring
    #return retornoJson
    return jsonify(retornoJson)

@app.route('/calculator/requestbody')
def do_calc_body():

    body = request.json
    validator = checkBody(body)

    if validator == False:
        retorno_error={
            "Message: " : "Faltou algum campo no body: operation, value1 ou value2"
        }
        return retorno_error, 400

    # com BODY e sem LIST
    operation = body["operation"]
    value1 = str(body["value1"])
    value2 = str(body["value2"])

    validator = checkData(operation, value1, value2)

    if validator == False:
        retorno_error={
            "Message: " : "Valores incorretos, precisa ser numerios value1 e value2. Ou se divisao, value2 nao pode ser 0"
        }
        return retorno_error, 400

    value1 = int(body["value1"])
    value2 = int(body["value2"])
    
    #match  operation: case "sum": somente PYTHON 3.10
    if operation == "sum":
            result = value1 + value2
    elif operation == "minus":
            result = value1 - value2
    elif operation == "multi":
            result = value1 * value2
    elif operation == "div":
            result = value1 / value2
    else:
         operation = "none"

    if operation == "none":
        retornoJson ={
         "resultado" : "operacao invalida",
         "Operation/Value1/Value2": [operation,value1,value2],
         "ExecOK?": False,
         "TypeRequisition": "Body_Param"
        }
        return retornoJson, 400
    else: 
        resultstring = str(result)
        
        arrayofobject = [
        {
            "operation": operation,
            "value1": value1
        },
        {
            "operation": operation,
            "value2": value2
        }
        ]

        retornoJson ={
         "resultado" : resultstring,
         "Operation/Value1/Value2/ArrayOfObject": [operation,value1,value2, arrayofobject],
         "ExecOK?": True,
         "TypeRequisition": "Body_Param"
        }
    #return "2 + 2 eh: " + calculostring
    #return retornoJson
    return jsonify(retornoJson)

@app.route('/calculator/requestbody/list')
def do_calc_body_list():

    body = request.json

    try:
        listparametros = body["listparameters"]
        operation = str(listparametros[0])
        value1 = str(listparametros[1])
        value2 = str(listparametros[2])
    except Exception as e:
        retorno_error={
            "Message: " : "Passe todos os parametros na LIST. Na ordem: Operation, Value1 e Value2"
        }
        return retorno_error, 400

    validator = checkData(operation, value1, value2)

    if validator == False:
        retorno_error={
            "Message: " : "Valores incorretos, precisa ser numerios value1 e value2. Ou se divisao, value2 nao pode ser 0"
        }
        return retorno_error, 400

    value1 = int(listparametros[1])
    value2 = int(listparametros[2])
    
    #match  operation: case "sum": somente PYTHON 3.10
    if operation == "sum":
            result = value1 + value2
    elif operation == "minus":
            result = value1 - value2
    elif operation == "multi":
            result = value1 * value2
    elif operation == "div":
            result = value1 / value2
    else:
         operation = "none"

    if operation == "none":
        retornoJson ={
         "resultado" : "operacao invalida",
         "Operation/Value1/Value2": [operation,value1,value2],
         "ExecOK?": False,
         "TypeRequisition": "Body_List"
        }
        return retornoJson, 400
    else: 
        resultstring = str(result)
        
        arrayofobject = [
        {
            "operation": operation,
            "value1": value1
        },
        {
            "operation": operation,
            "value2": value2
        }
        ]

        retornoJson ={
         "resultado" : resultstring,
         "Operation/Value1/Value2/ArrayOfObject": [operation,value1,value2, arrayofobject],
         "ExecOK?": True,
         "TypeRequisition": "Body_List"
        }
    #return "2 + 2 eh: " + calculostring
    #return retornoJson
    return jsonify(retornoJson)

def checkData(operator, value1, value2):
    if value1.isnumeric() != True or value2.isnumeric() != True:
        return False
    else:
        if operator == "div" and value2 == "0":
            return False
    return True
    
def checkBody(body):
    if "operation" not in body or "value1" not in body or "value2" not in body:
        return False
    
    return True

def checkParam(operation, value1, value2):
    if operation == "None" or value1 == "None" or value2 == "None":
        return False
    return True


    

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', debug=True)