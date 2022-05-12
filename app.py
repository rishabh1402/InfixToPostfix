import os
import flask
import urllib
import numpy as np
from flask import Flask, render_template, redirect, url_for, Response, request, session

app = Flask(__name__)

Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators
 
 
def infixToPostfix(expression): 

    stack = [] # initialization of empty stack

    output = ''  

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output+= character

        elif character=='(':  # else Operators push onto stack

            stack.append('(')

        elif character==')':

            while stack and stack[-1]!= '(':

                output+=stack.pop()

            stack.pop()

        else: 

            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:

                output+=stack.pop()

            stack.append(character)

    while stack:

        output+=stack.pop()

    return output

@app.route('/')
def home():
        return render_template("itop.html")

@app.route('/convert_i' ,methods=["GET", "POST"])
def convert_i():
	string = request.form.get("infix-po", False)
	output = infixToPostfix(string)
	f_output = ''.join(output)
	return render_template('itop_res.html', converted_text='{}'.format(f_output))
"""
@app.route('/itop')
def itop():
        return render_template("itop.html")
"""
if __name__ == "__main__":
    app.run(debug=True)

#exp = "a+b*(c^d-e)^(f+g*h)-i"


