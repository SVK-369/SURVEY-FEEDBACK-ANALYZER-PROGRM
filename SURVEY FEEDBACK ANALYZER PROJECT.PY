#Step1:preloaded (feedbacks given data)
feedback_data={'S_NO':[1,2,3,4,5,6,7,8,9,10],'Name':['Ravi','Meera','Sam','Anu','Raj','Divya','Arjun','Kiran','Leela','Nisha'],
        'Feedback':[' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print("--- Step 1: Preloaded Data Loaded Successfully ---")

#step2: add more feedbacks
num_new = int(input("Enter how many more feedbacks you  want to add: "))
start_S_NO = len(feedback_data['S_NO']) + 1

for i in range(num_new):
    print(f"\nEntering details for feedback #{start_S_NO+ i}:")
    name = input("Enter Name: ")
    feedback_text = input("Enter Written Feedback (text): ")
    rating = int(input("Enter Rating (1-5): "))
    
    feedback_data['S_NO'].append(start_S_NO + i)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback_text)
    feedback_data['Rating'].append(rating)
print("\n---step2:new feedbacks added successfully----")

#step3:text cleaning
cleaned_feedbacks = []

for text in feedback_data['Feedback']:
    text = text.lower()
    
    for p in ['.', ',', '!', '?']:
        text = text.replace(p, '')
        
    cleaned_text = ' '.join(text.split())
    cleaned_feedbacks.append(cleaned_text)
feedback_data['Feedback'] = cleaned_feedbacks
print("-----step3: text cleaningcompleted--")

#step4:word count insights
def count_word_in_feedbacks(word):
    count = 0
    target_word = word.lower()
    for text in feedback_data['Feedback']:
        words_in_feedback = text.split()
        if target_word in words_in_feedback:
            count += 1
    return count

print(f'Number of feedbacks containing "good": {count_word_in_feedbacks("good")}')
print(f'Number of feedbacks containing "poor": {count_word_in_feedbacks("poor")}')
print(f'Number of feedbacks containing "excellent": {count_word_in_feedbacks("excellent")}')
#step5:final summary insights 
print("\n--- Step 5: Final Summary & Insights ---")
print("\nFinal Cleaned Feedback Data:")
for key, value in feedback_data.items():
    print(f"{key}: {value}")
    #1.average ratings
ratings = feedback_data['Rating']
average_rating = sum(ratings) / len(ratings)
print(f"\nAverage Rating: {average_rating:.2f}")

#2,find longest comment
longest_comment = ""
max_words = 0
longest_name = ""

for name, text in zip(feedback_data['Name'], feedback_data['Feedback']):
    word_count = len(text.split())
    if word_count > max_words:
        max_words = word_count
        longest_comment = text
        longest_name = name

print(f"\nLongest Comment (by {longest_name} with {max_words} words):")
print(f'"{longest_comment}"')

#3. (Unique Words) 
unique_words = set()
for text in feedback_data['Feedback']:
    for w in text.split():
        unique_words.add(w)

print(f"\nList of Unique Words: {sorted(list(unique_words))}")

# 4.(Highest to Lowest)
combined_feedbacks = list(zip(feedback_data['S_NO'], feedback_data['Name'], feedback_data['Feedback'], feedback_data['Rating']))
sorted_feedbacks = sorted(combined_feedbacks, key=lambda x: x[3], reverse=True)

for sno, name, fb, rating in sorted_feedbacks:
    print(f"S_No: {sno} | Name: {name} | Rating: {rating} | Feedback: {fb}")
