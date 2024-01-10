from app import db,app
from app.models import Ticket, Flight, FlightRoute, ReceiptDetail
from sqlalchemy import func, case
import smtplib
from email.message import EmailMessage
import random
import string



def count_flight_by_route():
    return db.session.query(FlightRoute.id, FlightRoute.name, func.count(case((Flight.note != 0, Flight.id)))) \
        .join(Flight, Flight.flightRoute_id == FlightRoute.id, isouter=True) \
        .group_by(FlightRoute.id).all()



def stats_revenue(month=None):
    query = db.session.query(FlightRoute.id, FlightRoute.name, func.sum(ReceiptDetail.unit_price * ReceiptDetail.quantity)) \
        .join(ReceiptDetail, ReceiptDetail.flightRoute_id.__eq__(FlightRoute.id), isouter=True) \
        .group_by(FlightRoute.id, FlightRoute.name)

    # if month

    return query.group_by(FlightRoute.id).all()

def stats_revenue_by_month(year=2024):
    return db.session.query(func.extract('month', Ticket.created_date),
                            func.sum(ReceiptDetail.unit_price*ReceiptDetail.quantity))\
                     .join(ReceiptDetail, ReceiptDetail.ticket_id.__eq__(Ticket.id))\
                     .filter(func.extract('year', Ticket.created_date).__eq__(year))\
                     .group_by(func.extract('month', Ticket.created_date)).all()




def generate_otp():
    return str(random.randint(10000, 99999))


def send_mail(mailto, msg):
    email_from = 'giahuy261103@gmail.com'
    email_to = mailto
    password = 'xxce yrwo ffur xfws'
    subject = 'Email xác nhận tài khoản'
    body = msg
    em = EmailMessage()
    em['From'] = email_from
    em['To'] = email_to
    em['Subject'] = subject
    em.set_content(body)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_from, password)
        smtp.send_message(em)
        print('Check your email : ')

if __name__ == '__main__':
    with app.app_context():
        print(stats_revenue_by_month(2024))