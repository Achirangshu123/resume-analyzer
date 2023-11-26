import PyPDF2
import openai
import os

openai.api_key='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'

def readpdf(filepath):
    with open(filepath,'rb') as f:
        pdfreader=PyPDF2.PdfReader(f)
        no_pages=len(pdfreader.pages)
        text=""
        for page in range(no_pages):
            text+=pdfreader.pages[page].extract_text()
    return text 



def get_completion(prompt,model="gpt-3.5-turbo",temperature=0):
    messages=[{"role":"user","content":prompt}]
    response=openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

filepath='c:\\Users\\sonal\\Downloads\\resume.pdf'
resume= readpdf(filepath)

prompt=f"""
analyze the following resume delimited by triple backticks and ask the questions :
1.What programming languages is the candidate proficient in?
2.What company does the candidate currently work for?
3.Are references available for the candidate?

resume: ```{resume}```
"""
response=get_completion(prompt)
print(response)


        
    