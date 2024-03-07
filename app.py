from flask import Flask, render_template, request
import openai

app = Flask(__name__, static_folder='static', template_folder='templates')

# Set your OpenAI API key
openai.api_key = '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'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_text():
    user_input = request.form['user_input']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": "How can I assist you with Rainbow Six Siege?"}
        ],
        max_tokens=10
    )

    generated_text = response['choices'][0]['message']['content']
    return render_template('result.html', user_input=user_input, generated_text=generated_text)


if __name__ == '__main__':
    app.run(debug=True)
