import pandas as pd
import json
import openai
import langchain

def get_answered_questions(group_name):
    # Load the data from your Excel file
    df = pd.read_excel('wills questions.xlsx')

    # Remove rows with unanswered questions
    df = df.dropna(subset=['answers'])

    # Filter the dataframe to only include rows with the given group area
    filtered_df = df[df['group area'] == group_name]

    # If there are no answered questions in this group area, return None
    if filtered_df.empty:
        return None

    # Convert the filtered dataframe to a dictionary of the form {question: answer}
    question_answer_dict = dict(zip(filtered_df['parent question'], filtered_df['answers']))
    return question_answer_dict
def get_group_areas():
    # Load the data from your Excel file
    df = pd.read_excel('wills questions.xlsx')
    
    # Get a list of unique group areas
    group_areas = df['group area'].unique()
    
    return group_areas

def generate_will_part(group, will_examples, questions):
    """
    This function is responsible for generating a part of the will based on
    user-answered questions and examples from other wills.

    Parameters:
    - group (str): The group area for the will part to generate.
    - will_examples (list): A list of examples from other wills pertaining to the group area.
    - questions (dict): A dictionary of user-answered questions.

    Returns:
    - A string representing the generated part of the will.
    """
    # Prepare the messages for the OpenAI GPT-3.5-turbo model
    messages = [
        {
            "role": "system",
            "content": "You are an AI trained to assist in generating specific parts of a will document. You should use the information from user-answered questions and example wills to generate a proper and legally correct segment of a will. Your output should only cover the topics specifically mentioned in the user's answers and not include any details that were not provided by the user."
        },
        {
            "role": "user",
            "content": f"Generate a section of the will related to '{group}'. Please consider these three example wills: Will Example 1 - '{will_examples[0]}', Will Example 2 - '{will_examples[1]}', Will Example 3 - '{will_examples[2]}'. Also, take into account these specific answers from the user to the questions: {questions}. Your task is to generate a valid will section based on these inputs, while ensuring you only include details explicitly provided in the user's answers."
        }
    ]

    # Make the API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    # Extract the generated text
    generated_will_part = response['choices'][0]['message']['content'].strip()

    return generated_will_part



# Call the function with a group name and print the result
group_name = 'group area name'  # replace with the actual group name
print(get_answered_questions(group_name))


def read_will_json(file_name):
    with open(file_name) as f:
        return json.load(f)

# List of the will json files
will_files = ['will_1.json', 'will_2.json', 'will_3.json']

# Read each json file and store them in a list of dictionaries
wills = [read_will_json(file) for file in will_files]

# Get the unique group areas from the Excel file
group_areas = get_group_areas()

# Iterate through each group area
for group in group_areas:
    # Get the answered questions for this group
    question_answer_dict = get_answered_questions(group)

    # For each will, extract the data for this group area and call generate_will_part
    for will in wills:
        if group in will:
            generate_will_part(group, will[group], question_answer_dict)
