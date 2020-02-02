from flask import Flask, render_template, request
import fb_interact
import sorryeh

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apology', methods=['POST'])
def apology():
    firebase_app = fb_interact.FirebaseApp()

    # Extract webpage data
    section = request.form['section'] # cat
    subsection = request.form['subsection'] # sub_cat
    username = request.form['username'] # name
    reason = request.form['reason'] # reason

    # Example list arguments
    list_arg = ["test input 1", "test input 2", "test input 3"]

    # Store in Firebase application
    firebase_app.insert(section, subsection, list_arg)

    # Send to sorryeh analyzer
    apologies_prio = sorryeh.analyze(section, subsection, username, reason)
    return render_template('apology.html',
                           apgy_param_1=apologies_prio[0],
                           apgy_param_2=apologies_prio[1],
                           apgy_param_3=apologies_prio[2],
                           apgy_param_4=apologies_prio[3],
                           apgy_param_5=apologies_prio[4],
                           apgy_param_6=apologies_prio[5])

if __name__ == '__main__':
    app.run(host='127.0.0.1', threaded=True, debug=True)
