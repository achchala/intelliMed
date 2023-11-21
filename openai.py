#Note: The openai-python library support for Azure OpenAI is in preview.
import json
import os
import openai
import tools.files as files

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai_engine=os.getenv("OPENAI_ENGINE")

schema = files.get_schema()
sample_data = files.get_sampel_data()

sqlContent = f'''
  You are an RDBMS and SQL expert.
  You use the SQL schema provided between backquotes to provide SQL queries to provide the data requested by the user.
  `{schema}`
  Provide your answer using the following JSON template between backquotes:
  `{{
      "sql": "SELECT * FROM table_name WHERE condition",
      "description": "A short description of the query"
  }}`
  Always follow the following rules:
  - join clients and mpi.
  - join wv_vitals and clients.
  - join columns have the same name in both tables.
  - only use columns from the schema provided.
  - missing values in the tables are either NULL or empty.
  - always use LOWER function in your comparisons.
  - don't add any prefix or postfix to your answer
  Please note that:
  - patients demographic information is stored in [dbo].[mpi] table. 
  - patients vitals are stored in [dbo].[wv_vitals] table.
  - the names for the vitals are stored in [dbo].[wv_std_vitals] table.
  - patients visits to facilities are stored in the [dbo].[clients] table.
  Use the following data between backquotes for looking up vital names:
  `{sample_data}`
  '''


def get_sql(userContent):
    response = openai.ChatCompletion.create(
    engine=openai_engine,
    messages = [
        {"role":"system","content":sqlContent},
        {"role":"user","content":userContent},
        ],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    # print(response)
    response0 = response.choices[0].message.content.strip('`')
    sql = json.loads(response0)["sql"]
    # sql = response0.strip().strip("`")
    return sql

def provide_response(question, db_data):
    sysContent = f'''
    You are a health professional.
    I received the data between double backquotes from the database in response to the question between backquotes:
    question: `{question}`
    response: ``{db_data}``'''

    userContent = '''Use the data from the question and response and rewrite the response in a human readable form.'''
    response = openai.ChatCompletion.create(
    engine=openai_engine,
    messages = [
        {"role":"system","content":sysContent},
        {"role":"user","content":userContent},
        ],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

    # print(response)
    response0 = response.choices[0].message.content
    return response0