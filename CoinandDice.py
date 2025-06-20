import random

# Scenario A: Tossing a coin 10,000 times
def coin_toss_simulation(trials=10000):
    heads = 0
    tails = 0

    for _ in range(trials):
        toss = random.choice(["Heads", "Tails"])
        if toss == "Heads":
            heads += 1
        else:
            tails += 1

    print("🔄 Coin Toss Simulation:")
    print(f"Total Tosses: {trials}")
    print(f"Heads: {heads} ({heads/trials:.4f})")
    print(f"Tails: {tails} ({tails/trials:.4f})")
    print()

# Scenario B: Rolling two dice and computing probability of sum = 7
def dice_roll_simulation(trials=10000):
    sum_seven = 0

    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 7:
            sum_seven += 1

    print("🎲 Dice Roll Simulation:")
    print(f"Total Rolls: {trials}")
    print(f"Sum = 7: {sum_seven} times")
    print(f"Experimental Probability of sum 7: {sum_seven/trials:.4f}")
    print()

# Run both simulations
if __name__ == "__main__":
    coin_toss_simulation()
    dice_roll_simulation()
