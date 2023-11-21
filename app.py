import time
import tools.db as db 
import tools.openai as openai
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    question = request.json["prompt"] 

    sql = ""
    try:
        print("get_sql")
        sql = openai.get_sql(question)
    except Exception as e:
        return jsonify({"get_sql_error": str(e)})
        
    db_data = ""
    try:
        print("get_data")
        db_data = db.exec_query(sql)
    except Exception as e:
        return jsonify({"sql": sql, "get_data_error": str(e)})

    error = ""
    for i in range(5):
        try:
            print("get_response")
            response = openai.provide_response(question, db_data)
            return jsonify({"sql": sql, "data": db_data.strip("\n"), "response": response})
        except Exception as e:
            time.sleep(3)
            error = str(e)

    return jsonify({"sql": sql, "data": db_data, "get_response_error": error})


if __name__ == "__main__":
    app.run(debug=True)

# "give me a list of all vitals that don't have a short description",
# "give me demographic data about race of our patients""give me demographic data about race of our patients""give me the name and range of vitals",
# "give me the count of the patients with low, normal and high blood sugar",
# "give me percent of patients per province",
# "give me vital names and their average values for Elliott Abbott",
# "give me latest vitals names and values for Elliott Abbott",
# "give me the maximum pulse, temperature, blood sugar, o2 sats info for Elliott Abbott"
