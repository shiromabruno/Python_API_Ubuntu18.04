from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/calculator/requestparam')
def do_calc_param():
    operation = request.args.get("operation")
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

    # com BODY e sem LIST
    operation = body["operation"]
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

    listparametros = body["listparameters"]
    operation = listparametros[0]
    value1 = listparametros[1]
    value2 = listparametros[2]
    
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
    

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)