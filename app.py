# create a webserver using flask framework

# import all the required libraries

from flask import Flask, render_template, request, redirect, url_for
#import transformers
#from transformers import BloomForCausalLM
#from transformers import BloomForTokenClassification
#from transformers import BloomTokenizerFast
#import torch

#model_name = 'bigscience/bloom-1b1'
#tokenizer = BloomTokenizerFast.from_pretrained(model_name)
#model = BloomForCausalLM.from_pretrained(model_name)

# create a flask object
flask = Flask(__name__)

# create a route for the home page
@flask.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['textarea']
        return render_template('index.html', result= prompt + 'something')
        
    return render_template('index.html', result='what is the meaning of life?')

'''
def home_post(prompt):
    prompt = request.form['text']
    max_length = 150
    inputs = tokenizer(prompt, return_tensors='pt')
    
    bloom_model = tokenizer.decode(model.generate(inputs['input_ids'], max_length=max_length,do_sample=True,top_k=50,top_p=0.9)[0])
    chars_per_line = 75

    result = ''
    for i in range(0, len(bloom_model), chars_per_line):
        result += bloom_model[i:i+chars_per_line] + '\n'

    return render_template('index.html', result=result)
'''
# run the flask app
if __name__ == '__main__':
    flask.run(debug=True)
