import streamlit as st
import random

def hangman():
    words = ["apple", "banana", "orange"]
    chosen_word = random.choice(words)
    hidden_word = ["_" for _ in range(len(chosen_word))]
    attempts = 6

    # Initialize index for dynamic key generation
    input_index = 0

    st.write("Welcome to Hangman!")

    while attempts > 0:
        input_key = f"guess_{input_index}"

        guess = st.text_input(f"Enter a letter ({attempts} attempts left):", key=input_key)

        if guess:
            guess = guess.lower()  # Convert to lowercase if needed

            if len(guess) != 1 or not guess.isalpha():
                st.write("Invalid input. Please enter a single letter.")
                continue

            if guess in chosen_word:
                for i, letter in enumerate(chosen_word):
                    if letter == guess:
                        hidden_word[i] = letter
            else:
                attempts -= 1
                st.write("Incorrect guess. You have {} attempts remaining.".format(attempts))

            st.write(" ".join(hidden_word))

            if "".join(hidden_word) == chosen_word:
                st.write("You won!")
                break

            # Increment index for next unique key
            input_index += 1

    if attempts == 0:
        st.write("You lost. The word was:", chosen_word)

hangman()
