class GuessNumberGame():
    """
    Game Guess the number.
    """
    def __init__(self) -> None:
        from random import randint
    
        self.trays = 10
        self.min_number = 1
        self.max_number = 100
        self.user_enter = ''
        self.trays_count = 1
        self.robot_number = randint(self.min_number, self.max_number)
        
        #print ("\nRobot_number is:", self.robot_number, "\n")
        
        self.start()
        

    def check_user_enter(self, user_enter: str) -> bool:
        if self.user_enter.isdigit():
            return True
        return False

    def start(self) -> None:
        print("Guess the number game! For EXIT enter 'q'.")
        print(f"The robot has guessed a number from {self.min_number} to {self.max_number}, try to guess it (you have 10 attempts):\n")

        while self.trays_count <= self.trays:
            
            print("Attemp", self.trays_count)
            self.user_enter = input("Please enter the number: ")
            
            if self.check_user_enter(self.user_enter):
                self.user_enter = int(self.user_enter)
                self.trays_count += 1
            elif self.user_enter.lower() == "q":
                print("Bye...")
                exit(0)
            else:
                print("Error: Please enter only numbers\n")
                continue

            if self.max_number < self.user_enter or self.user_enter < self.min_number:
                print(f"Your number is out of range {self.min_number} to {self.max_number}! Try again.\n")
            elif self.robot_number == self.user_enter:
                print("You are winn!")
                exit(0)
            elif self.robot_number > self.user_enter:
                print("Your number is less! Try again.\n")
            elif self.robot_number < self.user_enter:
                print("Your number is more! Try again.\n")

        else:
            print("Tries exhaused!")

GuessNumberGame()