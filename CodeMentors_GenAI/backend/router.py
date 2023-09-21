## This is the page help you to underatnd how to use the completition and prompt module

from completition import getResponseLlm
import prompt
lang = "Python"
st = """
1. function name should follow snake case.
2. every function should have docstring
3. class name should start with Capital letter
"""

code = r"""
import pandas as pd
def getDataFrame():
    df == pd.read_csv('C:\Users\shivam.choudhary\Downloads\abc.csv')
    return df
"""

ready_prompt = prompt.optimizeCode(lang, st, code)
completition = getResponseLlm(ready_prompt)
print(completition)