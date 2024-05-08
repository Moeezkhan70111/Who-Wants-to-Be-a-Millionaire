questions = [
  "What is the capital of Australia?",
  "Which planet is known as the \"Red Planet\"?",
  "Who wrote the famous play \"Romeo and Juliet\"?",
  "What is the chemical symbol for gold?",
  "Which famous scientist was awarded the Nobel Prize in Physics for his theory of relativity?",
  "Who wrote the novel \"1984\"?",
  "Which country is the largest producer of coffee in the world?",
  "What is the longest bone in the human body?",
  "Who was the first woman to win a Nobel Prize?",
  "In which year was the Berlin Wall demolished?",
  "Who was the first woman to fly solo across the Atlantic Ocean?",
]

options = [
  ["a) Sydney", "b) Melbourne", "c) Canberra", "d) Perth"],
  ["a) Jupiter", "b) Venus", "c) Mars", "d) Saturn"],
  ["a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen", "d) Mark Twain"],
  ["a) Au", "b) Ag", "c) Pb", "d) Fe"],
  ["a) Isaac Newton", "b) Albert Einstein", "c) Stephen Hawking", "d) Galileo Galilei"],
  ["a) George Orwell", "b) Aldous Huxley", "c) J.D. Salinger", "d) Franz Kafka"],
  ["a) Brazil", "b) Colombia", "c) Ethiopia", "d) Vietnam"],
  ["a) Femur", "b) Tibia", "c) Fibula", "d) Humerus"],
  ["a) Marie Curie", "b) Mother Teresa", "c) Rosa Parks", "d) Jane Addams"],
  ["a) 1987", "b) 1989", "c) 1991", "d) 1993"],
  ["a) Amelia Earhart", "b) Bessie Coleman", "c) Harriet Quimby", "d) Jacqueline Cochran"],
]

correct_answers = [
  "d",  # Question 1
  "c",  # Question 2
  "b",  # Question 3
  "a",  # Question 4
  "b",  # Question 5
  "a",  # Question 6
  "a",  # Question 7
  "a",  # Question 8
  "a",  # Question 9
  "b",  # Question 10
  "a",  # Question 11
]

prize = ["1000$", "2000$", "4000$", "8000$", "16000$", "32000$", "64000$", "125000$", "250000$", "500000$", "1 Million$"]

def opt(i):
  for j in range(len(options[i])):
      print(options[i][j])
  print("\n")  

i = 0
milestone_reached = False

while i < len(questions):
  print(questions[i], "\n")
  opt(i)
  a = input("Enter Your Option: ")

  if a == correct_answers[i]:
      print("\nCongrats! You Won", prize[i], "\n")
      if prize[i] == "32000$":
          milestone_reached = True
          print("Do You Still Want to Play?")
          inp = input("Enter Y for \"Yes\" and N for \"No\": ")
          inplo = inp.lower()
          if inplo == "y":
              i += 1
          else:
              print("32000$ Transferred to your bank account.")
              break
      elif prize[i] == "1 Million$":
          print("Congrats! You Won the Game.")
          break
  else:
      if milestone_reached:
          print("You won 32000$")
      else:
          print("\nSorry! You Lost\n")
      break
  i += 1
