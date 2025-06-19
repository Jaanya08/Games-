import random
print("The keys for the game is:\nS for Snake\nW for Water\nG for Gun")
score_player=0
score_computer=0
def Game():
  score_player=0
  score_computer=0
  while(score_player<5 and score_computer<5):
    inp=input("Enter your choice: ")
    ch=random.choice(['S', 'W', 'G'])
    print(f"Computer's choice: {ch}")
    if(inp=='S' and ch=='W'):
      score_player+=1
    elif(inp=='W' and ch=='S'):
      score_computer+=1
    elif(inp=='W' and ch=='G'):
      score_player+=1
    elif(inp=='G' and ch=='W'):
      score_computer+=1
    elif(inp=='S' and ch=='G'):
      score_computer+=1
    elif(inp=='G' and ch=='S'):
      score_player+=1
    print(f"New Score:\nPlayer: {score_player}\nCompuetr: {score_computer}")
  if(score_player>score_computer):
    print("Congratulations! You Won!! 🥳")
  else:
    print("Computer Won!")
Game()
while True:
  inp=input("Enter 'P' to play again and 'E' to exit: ")
  if(inp=='P'):
    Game()
  else:
    break
print("Thanks for playing! 💕")