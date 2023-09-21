from langchain.llms import OpenAI
from connection import set_env

def getResponseLlm(prompt):
    try:
        set_env()
        llm = OpenAI()
        response = llm(prompt)
        return {"response_code":200, "completition": response}
    except Exception as e:
        return {"response_code":400,"message":e}
 
