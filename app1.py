from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'
questions = [
    {"question": "What does a physiotherapist primarily treat?", "options": ["Injuries", "Heart Disease", "Mental Illness", "Diabetes"], "answer": "Injuries"},
    {"question": "What is the primary goal of physiotherapy?", "options": ["Pain relief", "Mental well-being", "Muscle strengthening", "All of the above"], "answer": "All of the above"},
    {"question": "What therapy is used to treat back pain?", "options": ["Hydrotherapy", "Massage therapy", "Physiotherapy", "Chiropractic"], "answer": "Physiotherapy"},
    {"question": "Which body system does physiotherapy mainly target?", "options": ["Nervous system", "Respiratory system", "Musculoskeletal system", "Digestive system"], "answer": "Musculoskeletal system"},
    {"question": "What is an example of a physiotherapy modality?", "options": ["Ultrasound", "Massage", "TENS", "All of the above"], "answer": "All of the above"},
    {"question": "Which condition can physiotherapy help manage?", "options": ["Asthma", "Osteoarthritis", "Diabetes", "All of the above"], "answer": "All of the above"},
    {"question": "What is TENS in physiotherapy?", "options": ["Transcutaneous Electrical Nerve Stimulation", "Thermal Energy Neurological Stimulation", "Total Electrical Nerve Stimulation", "None of the above"], "answer": "Transcutaneous Electrical Nerve Stimulation"},
    {"question": "What role does physiotherapy play in post-surgical rehabilitation?", "options": ["Rest", "Rehabilitation", "Prevention", "None of the above"], "answer": "Rehabilitation"},
    {"question": "Which type of physiotherapy is used for neurological disorders?", "options": ["Neurophysiotherapy", "Cardiopulmonary physiotherapy", "Orthopedic physiotherapy", "Sports physiotherapy"], "answer": "Neurophysiotherapy"},
    {"question": "What is hydrotherapy?", "options": ["Water-based physical therapy", "Electric therapy", "Massage therapy", "A type of acupuncture"], "answer": "Water-based physical therapy"},
    {"question": "Which injury does physiotherapy often treat?", "options": ["Sprains", "Fractures", "Ligament tears", "All of the above"], "answer": "All of the above"},
    {"question": "What type of exercises are often used in physiotherapy?", "options": ["Strengthening", "Stretching", "Balance", "All of the above"], "answer": "All of the above"},
    {"question": "What is an orthosis used for in physiotherapy?", "options": ["To assist movement", "To monitor health", "To immobilize a body part", "To perform surgeries"], "answer": "To assist movement"},
    {"question": "Which of the following is commonly treated by physiotherapists?", "options": ["Spinal cord injuries", "Stroke rehabilitation", "Sports injuries", "All of the above"], "answer": "All of the above"},
    {"question": "What is a common symptom that physiotherapists treat?", "options": ["Muscle weakness", "Fatigue", "Chronic pain", "All of the above"], "answer": "All of the above"},
    {"question": "Which type of physiotherapy focuses on sports injuries?", "options": ["Sports physiotherapy", "Pediatric physiotherapy", "Cardiovascular physiotherapy", "Geriatric physiotherapy"], "answer": "Sports physiotherapy"},
    {"question": "What is the purpose of heat therapy in physiotherapy?", "options": ["Reduce swelling", "Increase blood flow", "Alleviate pain", "None of the above"], "answer": "Increase blood flow"},
    {"question": "What does a physiotherapist assess in a patient?", "options": ["Strength", "Range of motion", "Balance", "All of the above"], "answer": "All of the above"},
    {"question": "Which technique does physiotherapy use to improve flexibility?", "options": ["Stretching", "Massage", "Ultrasound", "TENS"], "answer": "Stretching"},
    {"question": "What does a physiotherapist do for a post-operative patient?", "options": ["Monitor diet", "Help with mobility", "Prescribe medication", "Perform surgery"], "answer": "Help with mobility"},
    {"question": "Which treatment is effective for reducing swelling?", "options": ["Ice therapy", "Heat therapy", "Massage", "Electrical stimulation"], "answer": "Ice therapy"},
    {"question": "What is the role of exercise in physiotherapy?", "options": ["Prevent injury", "Increase strength", "Improve flexibility", "All of the above"], "answer": "All of the above"},
    {"question": "How does physiotherapy help in managing arthritis?", "options": ["Pain relief", "Improved joint function", "Increased flexibility", "All of the above"], "answer": "All of the above"},
    {"question": "Which of the following is a common physiotherapy treatment for neck pain?", "options": ["Heat therapy", "Ultrasound", "Neck exercises", "All of the above"], "answer": "All of the above"},
    {"question": "What type of injury can be treated by a physiotherapist?", "options": ["Sprain", "Fracture", "Ligament injury", "All of the above"], "answer": "All of the above"},
    {"question": "What technique is commonly used to restore joint mobility?", "options": ["Joint mobilization", "Electrotherapy", "Massage", "TENS"], "answer": "Joint mobilization"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    session['player_name'] = name
    email = request.form['Email']
    session['Email'] = email
    return redirect(url_for('start'))

@app.route('/start')
def start():
    session['selected_questions'] = random.sample(questions, 5)
    session['current_question'] = 0
    session['score'] = 0
    return redirect(url_for('question', question_id=1))

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    if question_id > len(session['selected_questions']):
        return redirect(url_for('result'))

    if request.method == 'POST':
        selected_option = request.form.get('option')
        correct_answer = session['selected_questions'][question_id - 1]['answer']
        session['score'] += 1 if selected_option == correct_answer else 0
        return redirect(url_for('question', question_id=question_id + 1))

    question_data = session['selected_questions'][question_id - 1]
    return render_template('trivia.html', question=question_data, question_id=question_id)

@app.route('/result')
def result():
    score = session.get('score', 0)
    prize = {"type": "T-shirt", "images": "tshirt.gif"} if score > 3 else {"type": "Notebook", "images": "notebook.gif"} if score == 3 else None
    return render_template('result.html', score=score, total=len(session['selected_questions']), prize=prize)

if __name__ == '__main__':
    app.run(debug=True)

