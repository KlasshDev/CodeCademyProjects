# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # This is Jeopardy!

# %% [markdown]
# #### Overview

# %% [markdown]
# This project is slightly different than others you have encountered thus far. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you'll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and/or other resources when you encounter a problem that you cannot easily solve.

# %% [markdown]
# #### Project Goals

# %% [markdown]
# You will work to write several functions that investigate a dataset of _Jeopardy!_ questions and answers. Filter the dataset for topics that you're interested in, compute the average difficulty of those questions, and train to become the next Jeopardy champion!

# %% [markdown]
# ## Prerequisites

# %% [markdown]
# In order to complete this project, you should have completed the Pandas lessons in the <a href="https://www.codecademy.com/learn/paths/analyze-data-with-python">Analyze Data with Python Skill Path</a>. You can also find those lessons in the <a href="https://www.codecademy.com/learn/data-processing-pandas">Data Analysis with Pandas course</a> or the <a href="https://www.codecademy.com/learn/paths/data-science/">Data Scientist Career Path</a>.
#
# Finally, the <a href="https://www.codecademy.com/learn/practical-data-cleaning">Practical Data Cleaning</a> course may also be helpful.

# %% [markdown]
# ## Project Requirements

# %% [markdown]
# 1. We've provided a csv file containing data about the game show _Jeopardy!_ in a file named `jeopardy.csv`. Load the data into a DataFrame and investigate its contents. Try to print out specific columns.
#
#    Note that in order to make this project as "real-world" as possible, we haven't modified the data at all - we're giving it to you exactly how we found it. As a result, this data isn't as "clean" as the datasets you normally find on Codecademy. More specifically, there's something odd about the column names. After you figure out the problem with the column names, you may want to rename them to make your life easier for the rest of the project.
#    
#    In order to display the full contents of a column, we've added this line of code for you:
#    
#    ```py
#    pd.set_option('display.max_colwidth', None)
#    ```

# %%
import pandas as pd
# pd.set_option('display.max_colwidth', None)

Jeopardy = pd.read_csv('jeopardy.csv')
Jeopardy.rename(columns={'Show Number'  : 'show_number', 
                        ' Air Date'     : 'air_date',
                        ' Round'        : 'round',
                        ' Category'     : 'category',
                        ' Value'        : 'value',
                        ' Question'     : 'question',
                        ' Answer'       : 'answer'}, inplace=True)
print(Jeopardy.head(1))
print(Jeopardy.info())

# %% [markdown]
# 2. Write a function that filters the dataset for questions that contains all of the words in a list of words. For example, when the list `["King", "England"]` was passed to our function, the function returned a DataFrame of 49 rows. Every row had the strings `"King"` and `"England"` somewhere in its `" Question"`.
#
#    Test your function by printing out the column containing the question of each row of the dataset.

# %%
def search_questions(word_list, df):
    # Input: List of strings
    # Output: dataframe with questions containing all words from the list
    check = lambda question: all(str.lower(word) in str.lower(question) for word in word_list)
    result = df.loc[df['question'].apply(check)]
    return result
# %% [markdown]
# 3. Test your original function with a few different sets of words to try to find some ways your function breaks. Edit your function so it is more robust.
#
#    For example, think about capitalization. We probably want to find questions that contain the word `"King"` or `"king"`.
#    
#    You may also want to check to make sure you don't find rows that contain substrings of your given words. For example, our function found a question that didn't contain the word `"king"`, however it did contain the word `"viking"` &mdash; it found the `"king"` inside `"viking"`. Note that this also comes with some drawbacks &mdash; you would no longer find questions that contained words like `"England's"`.

# %%
print(search_questions(['programmer'], Jeopardy))

# %% [markdown]
# 4. We may want to eventually compute aggregate statistics, like `.mean()` on the `" Value"` column. But right now, the values in that column are strings. Convert the`" Value"` column to floats. If you'd like to, you can create a new column with float values.
#
#    Now that you can filter the dataset of question, use your new column that contains the float values of each question to find the "difficulty" of certain topics. For example, what is the average value of questions that contain the word `"King"`?
#    
#    Make sure to use the dataset that contains the float values as the dataset you use in your filtering function.

# %%
currencyFloat = lambda value: float(value[1:].replace(',','')) if value != "None" else 0
Jeopardy["value"] = Jeopardy["value"].apply(currencyFloat)

def difficulty(word_list, df):
    data = search_questions(word_list, df)
    # sumOfValues = data['value'].sum()
    # avgOfQuestion = sumOfValues / len(data)
    return data['value'].mean()

print(difficulty(['king'], Jeopardy))


# %% [markdown]
# 5. Write a function that returns the count of unique answers to all of the questions in a dataset. For example, after filtering the entire dataset to only questions containing the word `"King"`, we could then find all of the unique answers to those questions. The answer "Henry VIII" appeared 55 times and was the most common answer.

# %%
def sumOfAnsweres(word_list, df):
    '''
    Input : List of words
    Output: Dataframe with answeres and counts
    '''
    data = search_questions(word_list, df)
    
    
    return data['answer'].value_counts()

test = sumOfAnsweres(['king'], Jeopardy)
print(test)

# %% [markdown]
# 6. Explore from here! This is an incredibly rich dataset, and there are so many interesting things to discover. There are a few columns that we haven't even started looking at yet. Here are some ideas on ways to continue working with this data:
#
#  * Investigate the ways in which questions change over time by filtering by the date. How many questions from the 90s use the word `"Computer"` compared to questions from the 2000s?
#  * Is there a connection between the round and the category? Are you more likely to find certain categories, like `"Literature"` in Single Jeopardy or Double Jeopardy?
#  * Build a system to quiz yourself. Grab random questions, and use the <a href="https://docs.python.org/3/library/functions.html#input">input</a> function to get a response from the user. Check to see if that response was right or wrong.

# %%

# %% [markdown]
# ## Solution

# %% [markdown]
# 7. Compare your program to our <a href="https://content.codecademy.com/PRO/independent-practice-projects/jeopardy/jeopardy_solution.zip">sample solution code</a> - remember, that your program might look different from ours (and probably will) and that's okay!

# %% [markdown]
# 8. Great work! Visit <a href="https://discuss.codecademy.com/t/this-is-jeopardy-challenge-project-python-pandas/462365">our forums</a> to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that's okay! There are multiple ways to solve these projects, and you'll learn more by seeing others' code.

# %%
