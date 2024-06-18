from dotenv import load_dotenv
load_dotenv() # loading all the environemnt variables

import os
import sqlite3
import streamlit as st
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def fetchResponseFromLLM(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt,question])
    return response.text

def fetchSummaryFromLLM(question,answer):
    model=genai.GenerativeModel('gemini-pro')
    prompt = f'''
    You are an expert summarizing tool that takes the question and comma separated answers. Using that you 
    can generate a nice response. Please don't repeat the question and answer in the response!

    Question: {question}
    Answer: {answer}
     

    \n\nFor example,
    \nExample 1 - Question: How many customers have completed the purchase?, 
    Answer: 1
    Response: Only one customer has completed the purchase

    \nExample 2 - Question: Tell me count of all the clients browsing to the payment's screen but not purchasing?, 
    Answer: 3 
    Response: Three clients browsed the payment's screen but not completed the purchase

    '''

    print(prompt)
    response=model.generate_content(prompt)
    return response.text

def runSQLQuery(sql,database):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name CUSTOMER and has the following columns - CUSTOMER_NAME, AGE, 
    LANDING_SCREEN, PRODUCT_DETAILS, PAYMENT_SCREEN, FUlFILLMENT_SCREEN  \n\nFor example,
    \nExample 1 - How many customers have completed the purchase?, 
    the SQL command will be something like this SELECT COUNT(*) FROM CUSTOMER WHERE FUlFILLMENT_SCREEN = 1;
    \nExample 2 - Tell me count of all the clients browsing to the payment's screen but not purchasing?, 
    the SQL command will be something like this SELECT COUNT(*) FROM CUSTOMER WHERE PAYMENT_SCREEN = 1; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

st.set_page_config(page_title="Let's make writing sql easy")
st.subheader("Tabular Data making sense with GenAI")
st.divider()
question=st.text_input("What do you want to know ? ",key="input")
submit=st.button("Submit")

if submit:
    response=fetchResponseFromLLM(question,prompt[0])
    print(response)
    response=runSQLQuery(response,"customer.db")
    
    resp = ""
    for row in response:
        resp = resp + str(row)
    print(resp)
    resp = resp.replace('(','').replace('\'','').replace('\'','').replace(')','')
    finalResponse = fetchSummaryFromLLM(question,resp)
    st.write(finalResponse)
    st.session_state.user_input = question