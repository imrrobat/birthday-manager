from django import template
import jdatetime

register = template.Library()


@register.filter
def to_jalali(value):

    if not value:
        return ""

    jalali_date = jdatetime.date.fromgregorian(date=value)

    months = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]

    month_name = months[jalali_date.month - 1]

    return f"{jalali_date.day:02d}/{month_name}/{jalali_date.year}"

@register.filter
def age(birthday):

    if not birthday:
        return ""

    from datetime import date

    today = date.today()

    age = today.year - birthday.year

    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    return age




@register.filter
def days_until_birthday(birthday):

    if not birthday:
        return ""

    from datetime import date

    today = date.today()

    # تولد امسال
    next_birthday = date(
        today.year,
        birthday.month,
        birthday.day
    )

    # اگر تولد امسال گذشته باشد، تولد سال بعد
    if next_birthday < today:
        next_birthday = date(
            today.year + 1,
            birthday.month,
            birthday.day
        )

    return (next_birthday - today).days