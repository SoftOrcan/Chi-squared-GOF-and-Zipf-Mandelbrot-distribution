import re

# Read the html file
with open("Alice in Wonderland.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# Replace multiple spaces/newlines with a single space for word processing
cleaned_text = re.sub(r'\s+', ' ', raw_text).strip()

# Initialize a list to store all words
words = []
# Iterate through all words, split by " " (empty space)
for w in cleaned_text.split(" "):
    # Convert the word to lowercase
    w = w.lower()
    # If the word is not an empty space,
    if w:
        # Append the word to 'words'
        words.append(w)

# Create a dict to store the # of occurrences of the word and the probability of occurrence
# Probability of occurrence is calculated as # of occurrences of the word / total # of words
unique_words = {w: [0, 0] for w in words}

# Count the # of occurrences of each word
for w in words:
    # Increase by 1 for every occurrence of the word
    unique_words[w][0] += 1

# Sort the items in unique_words by descending order and get the top 20 words
sorted_top20 = dict(sorted(unique_words.items(), key=lambda item: item[1][0], reverse=True)[:20])

# Initialize the numerator and denominator of the Zipf-Mandelbrot distribution
numerator, denominator = 0, 0
# Iterate through the 20 ranks
for i in range(1, 21):
    # Calculate the denominator of the Zipf-Mandelbrot distribution
    denominator += 1 / (i + 2.7)

# Calculate the theoretical probability for each rank
theoretical_p = []
# Iterate through the 20 ranks
for i in range(1, 21):
    # Calculate the numerator of the Zipf-Mandelbrot distribution
    numerator = (1 / (i + 2.7))
    # Calculate the theoretical probability for each rank by dividing the numerator of the rank by the denominator constant
    theoretical_p.append(numerator / denominator)

# Output: [0.1367020048361731, 0.1076164718923065, 0.08873638910418255, 0.07549215192445381, 0.06568797634984942,
# 0.05813763424067133, 0.05214406370039594, 0.04727078671905052, 0.04323054853793509, 0.03982656833809768,
# 0.036919519554294934, 0.03440798761182589, 0.032216396044193664, 0.030287270532565302, 0.028576125304736754,
# 0.027047990261702702, 0.025674995832174648, 0.02443465786926766, 0.023308636769301408, 0.02228182457682117]
print(theoretical_p)

# Initialize a value to store the total top 20 words
total_top20 = 0
# Iterate through all values in the 20 words
for key, value in sorted_top20.items():
    # Compute the total # of occurrences for the top 20 words
    total_top20 += value[0]

# Initialize a list to store the expected # of words for each rank
expected_values = []
# Iterate through the 20 ranks
for i in range(20):
    # Calculate the expected # of words for each rank
    # Calculated by multiplying the total # of words by the Zipf-Mandelbrot distribution's probabilities for each rank
    expected_values.append(total_top20 * theoretical_p[i])

# Initialize the chi-squared value as 0
chi_squared = 0
# Initialize a value to iterate through all ranks
count = 0
# Iterate through all top 20 words
for key, value in sorted_top20.items():
    # Calculate the chi-squared value:
    # (Observed Value - Expected Value)^2 / Expected Value
    chi_squared += ((value[0] - expected_values[count]) ** 2) / expected_values[count]
    # Increase the count
    count += 1

# Output: 250.03891237497032
print(chi_squared)
