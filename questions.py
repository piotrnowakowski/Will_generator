import pandas as pd
import json

# Load your Excel file
df = pd.read_excel('wills questions.xlsx')

# Create a dictionary to store data
data = {}

# Loop through each row in the dataframe
for index, row in df.iterrows():
    group_area = row['Group Area']
    parent_question = row['Parent Question']
    answers = row['Answers']
    if_yes = row['If Yes']
    if_no = row['If No']

    # If group area doesn't exist in data, add it
    if group_area not in data:
        data[group_area] = {}
    
    # Add parent question, answers, if_yes, if_no to group area
    data[group_area][parent_question] = {
        'answer': answers,
        'if_yes': if_yes,
        'if_no': if_no
    }

# Write the data to a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)
