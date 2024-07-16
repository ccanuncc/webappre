from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'skey'

questions = [
    {
        'id': 1,
        'text': 'Python\'da yapay zeka geliştirmek için kullanılan kütüphane hangisidir?',
        'options': ['TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn', 'NumPy'],
        'correct_answer': 'TensorFlow'
    },
    {
        'id': 2,
        'text': 'Bilgisayar görüşünde kullanılan bir teknik hangisidir?',
        'options': ['Derin öğrenme', 'Doğal dil işleme', 'Görüntü işleme', 'Makine öğrenimi', 'Veri madenciliği'],
        'correct_answer': 'Görüntü işleme'
    },
    {
        'id': 3,
        'text': 'NLP ile ilgili olmayan seçenek hangisidir?',
        'options': ['Metin sınıflandırma', 'Konuşma tanıma', 'Görüntü işleme', 'Makine çevirisi', 'Duygu analizi'],
        'correct_answer': 'Görüntü işleme'
    },
    {
        'id': 4,
        'text': 'Python uygulamalarında AI modelleri uygulamak için kullanılan bir yöntem hangisidir?',
        'options': ['API\'ler', 'Kütüphaneler', 'Çerçeveler', 'Araçlar', 'Hepsi'],
        'correct_answer': 'Hepsi'
    }
]

@app.route('/')
def home():
    high_score = session.get('high_score', 0)
    return render_template('index.html', questions=questions, high_score=high_score)

@app.route('/submit', methods=['POST'])
def submit():
    results = []
    score = 0
    for question in questions:
        selected_option = request.form.get(f'option_{question["id"]}')
        if selected_option == question['correct_answer']:
            results.append(f"Soru {question['id']}: Doğru!")
            score += 1
        else:
            results.append(f"Soru {question['id']}: Yanlış. Doğru cevap: {question['correct_answer']}")
    
    total_questions = len(questions)
    score_percentage = (score / total_questions) * 100
    high_score = session.get('high_score', 0)
    
    if score_percentage > high_score:
        session['high_score'] = score_percentage
        high_score = score_percentage

    return render_template('result.html', results=results, score=score_percentage, total_questions=total_questions, high_score=high_score)

if __name__ == '__main__':
    app.run(debug=True)