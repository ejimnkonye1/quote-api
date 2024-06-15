from flask import Flask,request,jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)
@app.route('/quote')
def Joke():
    return "quote"
@app.route('/get_quote')
def get_quote():
    quote_data = {
        "quote1":{
          "quote_id": "quote1",
        "quote" :"\"The quieter you become, the more you can hear. This is the essence of centering.\"",
        "quote_author": " ~ Baba Ram Dass"
        },
        "quote2":{
            "quote_id": "quote2",
            "quote":"\"Data is not information, information is not knowledge, knowledge is not understanding, understanding is not wisdom.\"",
             "quote_author": "~ Clifford Stoll"

        },
        "quote3":{
            "quote_id": "quote3",
            "quote":"\"Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution.\"",
             "quote_author": "~ Albert Einstein"

        }
    }
    if  quote_data:
       # Convert dictionary values to a list and select a random element
       #we use random.choice
      random_quote_id = random.choice(list(quote_data.keys()))
      random_quote = quote_data[random_quote_id]
      return jsonify( random_quote)
    else:
     # Handle case when quote_id is not found

     return jsonify({"error": "quote not found"}), 404
if __name__ == "__main__":
    app.run(debug=True , port=8000)