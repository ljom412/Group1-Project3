from flask import Flask, send_file, render_template, jsonify

app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return f'''
#     <h1>ICO Coffee Dataset</h1>

#     <h3>Available routes:</h3>

#     <ul>
#         <li><a href="/pie_chart">Exports Pie Chart</a><li>
#     </ul>

# '''

# @app.route('/')
# def index():
#     # Data to populate the drop-down menu
#     options = ['Imports', 'Exports', 'Indicator Pricing']
#     return render_template('index.html', options=options)

# @app.route('/pie_chart')
# def display_pie_chart():
#     pie_chart_path = 'static/images/exports_pie_chart.png'

#     return send_file(pie_chart_path, mimetype='image/png')



## Route for the existing homepage
@app.route('/')
def homepage():
    # Data for the drop-down menu
    options = ['Exports', 'Option 2', 'Option 3']
    return render_template('homepage.html', options=options)

if __name__ == '__main__':
    app.run(debug=True)