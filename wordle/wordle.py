import random

WORDS = ["apple", "plant", "brick", "smart", "python", "teach", "night", "water", "radio", "magic"]


def show_guess(guess, target):
    result = ""
    for i in range(len(guess)):
        if guess[i] == target[i]:
            result += f"[🟩 {guess[i]}]"
        elif guess[i] in target:
            result += f"[🟨 {guess[i]}]"
        else:
            result += f"[⬛ {guess[i]}]"
    print(result)

def play():
    target = random.choice(WORDS)
    attempts = 6
    
    print("\n🎮 WORDLE - Terminal Edition")
    print("Guess the 5-letter word!\n")

    while attempts > 0:
        guess = input(f"{attempts} tries left → ").lower().strip()

        if len(guess) != 5:
            print("❗ Must be 5 letters!")
            continue

        if guess not in WORDS:
            print("❗ Not in word list!")
            continue

        show_guess(guess, target)

        if guess == target:
            print("\n🎉 Correct! You win!")
            return
        
        attempts -= 1

    print(f"\n💀 Out of tries! The word was: {target.upper()}")

if __name__ == "__main__":
    play()

