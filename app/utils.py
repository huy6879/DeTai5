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
    query = db.session.query(
        FlightRoute.id,
        FlightRoute.name,
        func.sum(ReceiptDetail.unit_price * ReceiptDetail.quantity).label('total_revenue')
    ) \
        .outerjoin(ReceiptDetail, ReceiptDetail.flightRoute_id.__eq__(FlightRoute.id)) \
        .group_by(FlightRoute.id, FlightRoute.name)

    if month is not None:
        query = query.filter(func.extract('month', ReceiptDetail.created_date) == month)

    return query.all()

    # Ví dụ sử dụng với tháng cụ thể (ví dụ: tháng 1)




def stats_revenue_by_year(year=None):
    query = db.session.query(
        func.extract('month', ReceiptDetail.created_date).label('month'),
        func.sum(ReceiptDetail.unit_price * ReceiptDetail.quantity).label('total_revenue')
    ) \
        .outerjoin(FlightRoute, FlightRoute.id == ReceiptDetail.flightRoute_id) \
        .group_by(func.extract('month', ReceiptDetail.created_date)) \
        .filter(func.extract('year', ReceiptDetail.created_date) == year)

    # Chuyển kết quả về list, điền các tháng không có doanh thu với giá trị 0
    result = {row[0]: row[1] for row in query.all()}
    for month in range(1, 13):
        if month not in result:
            result[month] = 0

    # Sắp xếp kết quả theo tháng
    sorted_result = sorted(result.items())
    return sorted_result




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
        print(stats_revenue(7))