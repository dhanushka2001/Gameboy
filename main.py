import gameboy

def main():
  while True:
    print("What game would you like to play?")
    a = input("| 1 = Higher/Lower | 2 = Twenty One Dares | 3 = Connect 4 |\n")
    allow = ["1", "2","3"]
    while a not in allow:
      print("Enter valid input")
      a = input("| 1 = Higher/Lower | 2 = Twenty One Dares | 3 = Connect 4 |\n")
    if a == "1":
      x = gameboy.HigherLower()
      x.menu()
    elif a == "2":
      x = gameboy.TwentyOneDares()
      x.menu()
    else:
      x = gameboy.ConnectFour()
      x.menu()

if __name__ == "__main__":
  main()
