import random
import json
import datetime

current_time = datetime.datetime.now()

secret = random.randint(1, 30)
attempts = 0

with open("score_list_2.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + ", secret number: " + score_dict["secret_number"]
          + ", Player name: " + score_dict["Player_name"] + ", Wrong guesses: " + score_dict["wrong_guesses"])


name = input("Unesite ime: ")

wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1


    if guess == secret:

        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "secret_number": str(secret),
                           "Player_name": name, "wrong_guesses": str(wrong_guesses)})

        with open("score_list_2.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)