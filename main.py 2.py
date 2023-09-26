# Define the Player class
class Player:
  # Define a method to play cricket
  def play(self):
    # Print a generic message
    print("The player is playing cricket.")


# Define the Batsman class as a subclass of Player
class Batsman(Player):
  # Override the play method
  def play(self):
    # Print a specific message
    print("The batsman is batting.")


# Define the Bowler class as a subclass of Player
class Bowler(Player):
  # Override the play method
  def play(self):
    # Print a specific message
    print("The bowler is bowling.")


# Create objects of both the Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play method for each object
batsman.play()  # The batsman is batting.
bowler.play()  # The bowler is bowling.
