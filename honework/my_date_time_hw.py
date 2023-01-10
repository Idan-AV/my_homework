# exercise2
import datetime


# def time_left1(date):
#     date_time_from_user = datetime.datetime.strptime(date, "%Y-%m-%d,%a,%H:%M%S %p")
#     my_now = datetime.datetime.now()
#     time_left = date_time_from_user - my_now
#     return time_left
#
#
# t = time_left1("2023-06-19,Mon,10:00 PM")
# print(t)


# exercise3
# def future_date(date):
#     user= datetime.datetime.strptime(date, "%d/%m/%Y")
#     time_now = datetime.datetime.now()
#     f = time_now + datetime.timedelta(days=1)
#     return f
#
#
# e = future_date("22/12/2022")
# print("the date of the upcoming friday of the date 22/12/2022 is : ", e)

# exercise 4
# def time_when_the_lecture_ends(date):
#     date_time_from_user = datetime.datetime.strptime(date, "%d/%m/%Y,%H:%M")
#     lecture_starts = datetime.datetime(2022, 12, 19, 17, 30)
#     t = date_time_from_user - lecture_starts
#     return t
#
#
# g = time_when_the_lecture_ends("19/12/2022,21:45")
# print(g)
