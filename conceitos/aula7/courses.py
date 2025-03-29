from flask import Flask, render_template

app = Flask(__name__)

@app.route('/courses')
def courses():
  courses = ['Python', 'Java', 'JavaScript', 'C#', 'C++', 'Ruby', 'PHP', 'Swift', 'Kotlin', 'Rust']
  return render_template('courses.html', courses=courses)

__name__ == '__main__' and app.run(debug=True)