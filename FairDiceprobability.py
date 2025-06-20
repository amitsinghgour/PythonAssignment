import random

def estimate_probability_of_six(trials=10000):
    success_count = 0

    for _ in range(trials):
        found_six = False
        for _ in range(10):
            if random.randint(1, 6) == 6:
                found_six = True
                break  # No need to roll further in this trial
        if found_six:
            success_count += 1

    probability = success_count / trials
    print(f"🎲 Estimated Probability of getting at least one '6' in 10 rolls: {probability:.4f}")

# Run the simulation
if __name__ == "__main__":
    estimate_probability_of_six()
