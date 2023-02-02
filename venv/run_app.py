import schedule
import smtplib
import time ,datetime
from flask import Flask, render_template, request
from apscheduler.schedulers.background import BackgroundScheduler
import info
from info import sender_password
from email.mime.text import MIMEText
from datetime import datetime, timedelta

appointments = []
app = Flask(__name__,template_folder='templates')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/schedule', methods=['POST'])
def schedule():
    # Get form data
    date = datetime.now().strftime("%Y-%m-%d")
    time = request.form.get('time')
    name = request.form.get('name')
    phone = request.form.get('phone')
    # Check availability
    if check_availability(time):
        appointments.append({ 'time': time, 'name': name,'phone':phone})

        # Send email
        send_email(name, time, phone)

        return render_template('thankyou.html')
    else:
        return render_template('sorry.html')

def send_email(name, time, phone):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("bazbenbaz0545@gmail.com", sender_password)

    # Build the message with all of the appointments
    msg = "The following appointments have been scheduled:\n\n"
    for appointment in appointments:
        msg += f"Name: {appointment['name']}\nTime: {appointment['time']}\nPhone: {appointment['phone']}\n\n"

    # Send the email
    server.sendmail("bazbenbaz0545@gmail.com", "bazbenbaz0545@gmail.com", msg)
    server.quit()




@app.route('/view')
def view():
    today_appointments = [appointment for appointment in appointments if appointment['time'] == datetime.now().strftime("%Y-%m-%-d")]
    return render_template( appointments=today_appointments)

def check_availability(time):
    # Compare the selected date and time with existing appointments
    for appointment in appointments:
        if appointment['time'] == time:
            return False
    return True

def remove_all_appointments():
    appointments.clear()

@app.route('/api', methods=['POST', 'GET'])
def api_response():
    from flask import jsonify
    if request.method == 'POST':
        return jsonify(**request.json)



if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(remove_all_appointments, 'interval', seconds=43200)
    scheduler.start()
    app.run(debug=True,port=3000,host='0.0.0.0')
















####שינוי אפליקציה
# import schedule
# import smtplib
# import time ,datetime
# from flask import Flask, render_template, request
# from apscheduler.schedulers.background import BackgroundScheduler
# import info
# from info import sender_password
# from email.mime.text import MIMEText
# from datetime import datetime, timedelta
#
# appointments = []
# app = Flask(__name__,template_folder='templates')
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/schedule', methods=['POST'])
# def schedule():
#     # Get form data
#     date = datetime.now().strftime("%Y-%m-%d")
#     time = request.form.get('time')
#     name = request.form.get('name')
#     phone = request.form.get('phone')
#     # Check availability
#     if check_availability(time):
#         appointments.append({ 'time': time, 'name': name,'phone':phone})
#
#         # Send email
#         send_email(name, time, phone)
#
#         return " Thank You !"
#     else:
#         return "Sorry, that time is not available "
#
# def send_email(name, time, phone):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login("bazbenbaz0545@gmail.com", sender_password)
#
#     # Build the message with all of the appointments
#     msg = "The following appointments have been scheduled:\n\n"
#     for appointment in appointments:
#         msg += f"Name: {appointment['name']}\nTime: {appointment['time']}\nPhone: {appointment['phone']}\n\n"
#
#     # Send the email
#     server.sendmail("bazbenbaz0545@gmail.com", "bazbenbaz0545@gmail.com", msg)
#     server.quit()
#
#
#
#
# @app.route('/view')
# def view():
#     today_appointments = [appointment for appointment in appointments if appointment['time'] == datetime.now().strftime("%Y-%m-%-d")]
#     return render_template( appointments=today_appointments)
#
# def check_availability(time):
#     # Compare the selected date and time with existing appointments
#     for appointment in appointments:
#         if appointment['time'] == time:
#             return False
#     return True
#
# def remove_all_appointments():
#     appointments.clear()
#
# @app.route('/api', methods=['POST', 'GET'])
# def api_response():
#     from flask import jsonify
#     if request.method == 'POST':
#         return jsonify(**request.json)
#
#
#
# if __name__ == '__main__':
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(remove_all_appointments, 'interval', seconds=43200)
#     scheduler.start()
#     app.run(debug=True,port=3000,host='0.0.0.0')

















































###final code with messages but the email is empty #####
# import schedule
# import smtplib
# import time ,datetime
# from flask import Flask, render_template, request
# from apscheduler.schedulers.background import BackgroundScheduler
# from twilio.rest import Client
# import info
# from info import sender_password
# from datetime import datetime, timedelta
#
#
# app = Flask(__name__)
# appointments = []
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/schedule', methods=['POST'])
# def schedule():
#     # Get form data
#     date = datetime.now().strftime("%Y-%m-%d")
#     time = request.form.get('time')
#     name = request.form.get('name')
#     phone = request.form.get('phone')
#     # Check availability
#     if check_availability(time):
#         appointments.append({  'time': time, 'name': name,'phone':phone})
#
#         # Send email
#         send_email(name, time, phone)
#
#         return "Appointment scheduled for " + name + " on " + " at " + time + ' his phone ' + phone
#     else:
#         return "Sorry, that time is not available "
#
# def send_email(name, time, phone):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login("bazbenbaz0545@gmail.com",sender_password)
#     msg = f"An appointment has been scheduled with {name} at {time} on his phone {phone}"
#     # server.sendmail("bazbenbaz0545@gmail.com", "bazbenbaz0545@gmail.com", msg)
#     # server.sendmail('',"bazbenbaz0545@gmail.com",msg)
#     server.sendmail('', "bazbenbaz0545@gmail.com", msg)
#
#     server.quit()
#
#
# @app.route('/view')
# def view():
#     today_appointments = [appointment for appointment in appointments if appointment['time'] == datetime.now().strftime("%Y-%m-%-d")]
#     return render_template('view.html', appointments=today_appointments)
#
# def check_availability(time):
#     # Compare the selected date and time with existing appointments
#     for appointment in appointments:
#         if appointment['time'] == time:
#             return False
#     return True
#
# def remove_all_appointments():
#     appointments.clear()
#
# if __name__ == '__main__':
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(remove_all_appointments, 'interval', seconds=43200)
#     scheduler.start()
#     app.run(debug=True,port=8000,host='0.0.0.0')

###final code with messages but the email is empty #####






























####Final code without messages####
# import schedule
# import time ,datetime
# from flask import Flask, render_template, request
# from apscheduler.schedulers.background import BackgroundScheduler
# from twilio.rest import Client
# import info
# from info import Sid ,token ,my_phone ,twilio_phone
# from datetime import datetime, timedelta
# app = Flask(__name__)
# appointments = []
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/schedule', methods=['POST'])
# def schedule():
#     # Get form data
#     date = datetime.now().strftime("%Y-%m-%d")
#     time = request.form.get('time')
#     name = request.form.get('name')
#     phone = request.form.get('phone')
#     # if not all([time, name, phone]):
#     #     return "Bad request"
#     # Check availability
#     if check_availability(time):
#         appointments.append({  'time': time, 'name': name,'phone':phone})
#
#         return "Appointment scheduled for " + name + " on " + " at " + time + ' his phone ' + phone
#     else:
#         return "Sorry, that time is not available "
#
#
# @app.route('/view')
# def view():
#     today_appointments = [appointment for appointment in appointments if appointment['time'] == datetime.now().strftime("%Y-%m-%-d")]
#     return render_template('view.html', appointments=today_appointments)
#
# def check_availability(time):
#     # Compare the selected date and time with existing appointments
#     for appointment in appointments:
#         if appointment['time'] == time:
#             return False
#     return True
#
# def remove_all_appointments():
#     appointments.clear()
#
# if __name__ == '__main__':
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(remove_all_appointments, 'interval', seconds=43200)
#     scheduler.start()
#     app.run(debug=True,port=8000,host='0.0.0.0')
####Final code without messages####













###################################################################

# 5QYv5HVlMiZQMJsoxQ1cHTafaern2tvjf9bSkAk0







# import schedule
# import time ,datetime
# from flask import Flask, render_template, request
# from apscheduler.schedulers.background import BackgroundScheduler
# from twilio.rest import Client
# import info
# from info import Sid ,token ,my_phone ,twilio_phone
# from datetime import datetime, timedelta
# app = Flask(__name__)
# appointments = []
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# #@app.route('/schedule', methods=['POST'])
# @app.route('/schedule', methods=['POST'])
# def schedule():
#     # Get form data
#     date = datetime.now().strftime("%Y-%m-%d")
#     time = request.form.get('time')
#     name = request.form.get('name')
#     phone = request.form.get('phone')
#     if not all([time, name, phone]):
#         return "Bad request"
#     # Check availability
#     if check_availability(time):
#         appointments.append({ 'date': date, 'selected_time': time, 'name': name,'phone':phone})
#
#         # Send text message
#         account_sid = Sid
#         auth_token = token
#         client = Client(account_sid, auth_token)
#         message = client.messages.create(
#             body="Appointment scheduled for " + name + " on " +  date + " at " + time + ' his phone ' + phone ,
#             from_= twilio_phone,
#             to=my_phone
#         )
#
#         return "Appointment scheduled for " + name + " on " + date + " at " + time + ' his phone ' + phone
#     else:
#         return "Sorry, that time is not available "
#
#
# @app.route('/view')
# def view():
#     today_appointments = [appointment for appointment in appointments if appointment['date'] == datetime.now().strftime("%Y-%m-%-d")]
#     return render_template('view.html', appointments=today_appointments)
#
# def check_availability(time):
#     # Compare the selected date and time with existing appointments
#     for appointment in appointments:
#         if appointment['selected_time'] == time:
#             return False
#     return True
#
# def remove_all_appointments():
#     appointments.clear()
#
# if __name__ == '__main__':
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(remove_all_appointments, 'interval', seconds=43200)
#     scheduler.start()
#     app.run(debug=True,port=8000,host='0.0.0.0')
#
#
#
#
#
#
# ###################################################################
