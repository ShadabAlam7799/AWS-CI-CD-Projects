from flask import Flask, request, render_template

application = Flask(__name__)
app = application

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Collecting form data
            gender = request.form.get('gender')
            ethnicity = request.form.get('ethnicity')
            parental_education = request.form.get('parental_level_of_education')
            lunch = request.form.get('lunch')
            test_preparation = request.form.get('test_preparation_course')
            reading_score = float(request.form.get('reading_score'))
            writing_score = float(request.form.get('writing_score'))

            # Dummy prediction logic (averaging scores)
            math_score_prediction = (reading_score + writing_score) / 2

            return render_template('home.html', 
                                   results=round(math_score_prediction, 2),
                                   gender=gender,
                                   ethnicity=ethnicity,
                                   parental_education=parental_education,
                                   lunch=lunch,
                                   test_preparation=test_preparation)
        except ValueError:
            return render_template('home.html', error="Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
