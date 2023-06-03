import time

def get_typing_speed(sentence):
  start_time = time.time()
  user_input = input(sentence)
  end_time = time.time()
  words = user_input.split()
  correct_words = 0
  for word in words:
    if word in sentence:
      correct_words += 1
  words_per_minute = (correct_words * 60) / (end_time - start_time)
  return words_per_minute

def main():
  sentences = ["The quick brown fox jumps over the lazy dog.", "I love to code in Python.", "This is a test sentence."]
  for sentence in sentences:
    typing_speed = get_typing_speed(sentence)
    print("Start typing the sentences.")
    print(f"Your typing speed for the sentence '{sentence}' is {typing_speed} words per minute.")

if __name__ == "__main__":
  main()
