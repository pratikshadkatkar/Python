feedback = input("Enter your feedback: ")

target_words = ["bad", "boring", "uninteractive"]

for word in target_words:
    feedback = feedback.replace(word, "****")

print("Moderated Feedback:")
print(feedback)