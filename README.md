# SURVEY-FEEDBACK-ANALYZER-PROGRM
SURVEY FEEDBACK ANALYZER PROGRAM
Overview of the Project:
​The goal of this program is to build a text-based feedback analysis tool in Python. It handles preloaded customer feedback, allows adding new feedback entries, cleans textual data, performs word count searches, and generates final analytical summaries like average ratings and unique words.

Explanation: This block initializes a Python dictionary named feedback_data preloaded with 10 records.  
​It organizes the data into four keys ('S_No', 'Name', 'Feedback', and 'Rating'), where each key holds a list of 10 items representing serial numbers, customer names, raw text comments, and numerical ratings (1–5).

Step 2: Add More Feedbacks
Explanation:
​num_new = int(input(...)) asks the user how many additional feedback entries they want to insert.  
​start_sno = len(feedback_data['S_No']) + 1 automatically computes the next starting serial number dynamically (since there are 10 items, len is 10, so 10 + 1 = 11).  
​The for loop runs num_new times, prompting the user for the Name, written Feedback (text), and an integer Rating (1–5) for each new entry.  
​.append() adds each new piece of data into its respective list inside the feedback_data diction


Step 3: Text Cleaning

​Explanation: This section loops through every raw feedback string to normalize and clean the text:  
​text.lower() converts all characters to lowercase so that words like "GOOD", "Good", and "good" are treated uniformly.
​The inner loop iterates through punctuation marks (., ,, !, ?) and uses .replace(p, '') to strip them out completely.  
​' '.join(text.split()) splits the string into individual words (discarding extra whitespaces) and rejoins them using a single space, removing any leading, trailing, or duplicate spaces.  
​Finally, the cleaned feedback list replaces the original raw feedbacks in the dictionary.

Step 4: Word Count Insights


​Explanation:
​A custom function count_word_in_feedbacks(word) is defined. It accepts a target search word, converts it to lowercase, and checks how many cleaned feedback entries contain that exact word.  
​text.split() breaks each feedback comment into a list of words, and target_word in words_in_feedback checks for a match. If found, the counter increases by 1.  
​The function is then called for the keywords "good", "poor", and "excellent" to print their occurrence frequencies.


Step 5: Final Summary & Insights


: ​Explanation:
​A custom function count_word_in_feedbacks(word) is defined. It accepts a target search word, converts it to lowercase, and checks how many cleaned feedback entries contain that exact word.  
​text.split() breaks each feedback comment into a list of words, and target_word in words_in_feedback checks for a match. If found, the counter increases by 1.  
​The function is then called for the keywords "good", "poor", and "excellent" to print their occurrence frequencies.
​Unique Words: Utilizes a Python set (which naturally drops duplicate entries) to store every single unique word used across all comments, and prints them in alphabetical order via sorted().  
​Sorting (Optional): Combines all columns together using zip(), then uses sorted() with a lambda function pointing to index 3 (the rating column) in descending order (reverse=True) to list entrie
from highest rating to lowest rating.

 ​Explanation:
​A custom function count_word_in_feedbacks(word) is defined. It accepts a target search word, converts it to lowercase, and checks how many cleaned feedback entries contain that exact word.  
​text.split() breaks each feedback comment into a list of words, and target_word in words_in_feedback checks for a match. If found, the counter increases by 1.  
​The function is then called for the key.




