from app import app,request,render_template,model,df
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        inp = request.form['pesan']
        predict = model.predict([inp])
        hasil = ""
        if 1 in predict :
            hasil = "CHAT PROMOSI"
        elif 2 in predict:
            hasil= "CHAT PORNOGRAFI"
        else:
            hasil= "CHAT PENIPUAN"
        return render_template('dashboard.html',hasil=hasil,data=df,p=str(predict))


    return render_template('dashboard.html',data=df)
