class Appointment:
    def __init__(self, time, name,phone):
        # self.date = date
        self.time = time
        self.name = name
        self.phone =phone

class Scheduler:
    def __init__(self):
        self.appointments = []

    def make_appointment(self,  time, name,phone):
        appointment = Appointment( time, name,phone)
        self.appointments.append(appointment)
        print("Appointment scheduled for " + name + " on "  + " at " + time)


    def view_appointments(self):
        for appointment in self.appointments:
            print("Name: " + appointment.name)
            print("phone: " + appointment.phone)
            # print("Date: " + appointment.date)
            print("Time: " + appointment.time)

scheduler = Scheduler()
scheduler.make_appointment("01/01/2022", "10:00 AM", "Muhammad","123")
scheduler.make_appointment("01/02/2022", "11:00 AM", "Asayel","123")
scheduler.view_appointments()
