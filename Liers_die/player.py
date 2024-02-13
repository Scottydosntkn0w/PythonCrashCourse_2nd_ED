from die import Die

class Player:

    def __init__(self) -> None:
        self.Number_of_Dice = 6
        self.Name = "None"
        self.Dice = [Die() for i in range(self.Number_of_Dice)]
    def roll_dice(self):
        results = []
        for roll_num in range(self.Number_of_Dice):
            self.result = Die.roll(self)
            results.append(self.result)

        # Analyze the results
        frequencies = []
        for value in range(1, Die.num_sides+1):
            frequency = results.count(value)
            frequencies.append(frequency)
            print(frequencies)

