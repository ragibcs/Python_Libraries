from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/math', methods=['POST'])
def math_operation():
    if request.method == 'POST':
        operation= request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])

    if operation == 'add':
        r = num1 + num2
        result = f"The sum of {num1} and {num2} is {r}"

    elif operation == 'subtraction':
        r = num1 - num2
        result = f"The difference of {num1} and {num2} is {r}"

    elif operation == 'multiply':
        r = num1 * num2
        result = f"The product of {num1} and {num2} is {r}"

    elif operation == 'divide':
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            r = num1 / num2
            result = f"The division of {num1} and {num2} is {r}"
    else:
        result = "Invalid operation"

    return render_template("result.html", result=result, operation=operation, num1=num1, num2=num2)

app.route('/via_postman',methods=["POST"])

def math_operation_via_postman():
    data = request.get_json()

    operation = data['operation']
    num1 = int(data['num1'])
    num2 = int(data['num2'])

    if operation == 'add':
        r = num1 + num2
        result = f"The sum of {num1} and {num2} is {r}"

    elif operation == 'subtraction':
        r = num1 - num2
        result = f"The difference of {num1} and {num2} is {r}"

    elif operation == 'multiply':
        r = num1 * num2
        result = f"The product of {num1} and {num2} is {r}"

    elif operation == 'divide':
        if num2 == 0:
            return jsonify("Cannot divide by zero")
        r = num1 / num2
        result = f"The division of {num1} and {num2} is {r}"

    else:
        return jsonify("Invalid operation")

    return jsonify(result)

if __name__ == '__main__':
    print("This app is working")
    app.run(debug=True)
