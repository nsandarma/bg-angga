from app import app,render_template,redirect,request,predict

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        pesan = request.form['pesan']
        hasil = predict(pesan)
        return f'{hasil}'
    return render_template('home.html')

        