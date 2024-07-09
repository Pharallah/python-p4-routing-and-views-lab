#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:num>')
def count(num):
    prnt = ''
    for num in range(num):
        prnt += f'{str(num)}\n'
    return prnt

@app.route('/math/<int:num1>/<string:op>/<int:num2>')
def math(num1, op, num2):
    # operands = ['+', '-', '*', '%']
    if op == "+":
        result = num1 + num2
        return str(result)
    elif op == "-":
        result = num1 - num2
        return str(result)
    elif op == "*":
        result = num1 * num2
        return str(result)
    elif op == "%":
        result = num1 % num2
        return str(result)
    elif op == 'div':
        result = num1 / num2
        return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
