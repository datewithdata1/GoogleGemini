import google.generativeai as genai
from dotenv import load_dotenv
import os
import sqlite3
import streamlit as st
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM App")


def get_gemini_response(question,prompt):
    response = model.generate_content([prompt,question])
    return response.text

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows

# Example usage
prompt = (
    "You are an expert SQL query writer. Given a question about a student database table with the following columns: "
    "id, name, subject, class, grade, and marks, generate an appropriate SQL query that will retrieve the relevant information."
    "Database name is student"
    "\n\n"
    "Question: "
    "Dont include ``` in beginning and end "
)


question = st.text_input("Question : ",key = "question")
submit = st.button("Ask the question?")

if submit and question:
    sql_query = get_gemini_response(question, prompt)
    st.subheader("The response is ")
    st.code(sql_query,language='sql')
    print(sql_query)
    rows = read_sql_query(sql_query,'students.db')
    st.subheader("Output : ")
    for row in rows:
        st.write(row)
    