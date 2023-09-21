def suggestChange(language, standard, code):
    prompt = f"""
    You are my code mentor, here are some coding standard to follow and {language} code written below, only suggest the changes as per coding standard
    coding standard: 
        {standard}

    code:
        {code}
    """
    return prompt

def constructCode(language, standard, code):
    prompt = f"""
    You are my code mentor, here are some coding standard to follow and {language} code written below, modify the code as per coding standard
    coding standard: 
        {standard}

    code:
        {code}
    """
    return prompt


def optimizeCode(language, code):
    '''
    method can be used to make you code time and space efficient
    '''
    prompt = f"""Task: You will be provided with a piece of {language} code and your task is to provide more efficienct code with respect to time and space complexity.
    Code:
    {code}
    """
    return prompt