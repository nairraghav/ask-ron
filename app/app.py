from flask import Flask, render_template, request
from random import randint, choice
from time import sleep

APP = Flask("ask_ron")
POSSIBLE_ANSWERS = ("As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                    "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
                    "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
                    "Yes.", "Yes – definitely.", "You may rely on it.")


@APP.route("/", methods=["GET"])
def get_home_page():
    return render_template("home.html")


@APP.route("/ask", methods=["POST"])
def ask_question():
    global POSSIBLE_ANSWERS
    question = request.form["question"]
    answer = choice(POSSIBLE_ANSWERS)
    sleep(randint(1, 3))
    return render_template("home.html", question=question, answer=answer)
