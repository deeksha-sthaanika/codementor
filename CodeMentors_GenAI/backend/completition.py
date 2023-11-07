from langchain.llms import OpenAI
from connection import set_env

def getResponseLlm(prompt):
    try:
        set_env()
        llm = OpenAI()
        response = llm(prompt)
        print(response)
        return {"response_code":200, "completition": response}
    except Exception as e:
        print("error:>>",e)
        return {"response_code":400,"message":e}
 
