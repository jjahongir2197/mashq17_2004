@app.route('/result13', methods=['GET', 'POST'])
def result13():
    res = None
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        date = request.form.get('date', '').strip()
        age_str = request.form.get('age', '').strip()

        try:
            age = int(age_str)
            age_togri = 18 <= age <= 99
        except ValueError:
            age_togri = False

        if len(name) > 2 and date and age_togri:
            res = [name, date, age]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result13.html', res=res)
