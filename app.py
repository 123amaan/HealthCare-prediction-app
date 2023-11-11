import numpy as np   
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form.get('Gender',False)
        if(Gender == 'Male'):
            Male = 0
        elif(Gender == 'Female'):
            Female = 1
        elif(Gender == 'Others'):
            Others = 2
            
        self_employed = request.form['self_employed']
        if(self_employed == 'Yes'):
            Yes = 1
        elif(self_employed == 'No'):
            No = 0
            
        family_history = request.form['family_history']
        if(family_history == 'Yes'):
            Yes = 1
        elif(family_history == 'No'):
            No = 0
            
        work_interfere = request.form['work_interfere']
        if(work_interfere == 'Sometimes'):
            Sometimes = 0
        elif(work_interfere == 'Never'):
            Never = 1
        
        elif(work_interfere == 'Rarely'):
            Rarely = 2
        elif((work_interfere == 'Often')):
            Often = 3
            
        remote_work = request.form['remote_work']
        if(remote_work == 'Yes'):
            Yes = 1
        elif(remote_work == 'No'):
            No = 0
        
            
        benefits = request.form['benefits']
        if(benefits == 'Yes'):
           Yes = 1
        elif(benefits == 'No'):
            No = 0 
        elif(benefits == 'Dont Know'):
            DontKnow = 2
            
        anonymity = request.form['anonymity']
        if(anonymity == 'Yes'):
           Yes = 1
        elif(anonymity == 'No'):
            No = 0 
        elif(anonymity == 'Dont Know'):
            DontKnow = 2
            
            
        mental_health = request.form['mental_health']
        if(mental_health == 'Yes'):
           Yes = 1
        elif(mental_health == 'No'):
            No = 0 
        elif(mental_health == 'Maybe'):
            Maybe = 2
            
        phys_health = request.form['phys_health']
        if(phys_health == 'Yes'):
           Yes = 1
        elif(phys_health == 'No'):
            No = 0 
        elif(phys_health == 'Maybe'):
            Maybe = 2
            
            
        prediction = model.predict([[46,0,0,0,3,1,1,2,2,0]])
        if prediction==0:
             return render_template('index.html',prediction_text="The Patient is in good condition")
        else:
             return render_template('index.html',prediction_text="The Patient is not in good condition")
         
if __name__ == '__main__':
    app.run(debug=True)