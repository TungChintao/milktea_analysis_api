from sqlalchemy import func
from app.models import Shop
from app.libs.extensions import db


def get_brand_detail(brand):
    query_data = db.session.query(Shop.city, Shop.avgprice, func.count(Shop.title)).filter(Shop.title == brand).group_by('city').all()
    resp_data = []
    city_num = 0
    for data in query_data:
        city_num += 1
        coordinate = db.session.query(Shop.latitude, Shop.longitude).filter(Shop.city == data[0]).first()
        resp_data.append({
            'city': data[0],
            'avgprice': data[1],
            'shopnum': data[2],
            'latitude': coordinate[0],
            'longitude': coordinate[1]
        })
    return city_num, resp_data


def get_price_area(left, right, brand):
    query_data = db.session.query(func.count(Shop.shopid)).filter(Shop.title == brand, Shop.avgprice > left, Shop.avgprice <= right).group_by('title').all()
    return query_data


def get_score_area(left, right, brand):
    query_data = db.session.query(func.count(Shop.shopid)).filter(Shop.title == brand, Shop.avgscore > left, Shop.avgscore <= right).group_by('title').all()
    return query_data


def get_brand_price(brand):
    query_data = db.session.query(func.max(Shop.avgprice), func.min(Shop.avgprice), func.avg(Shop.avgprice)).filter(Shop.isMain == 1, Shop.record == 1, Shop.title == brand).group_by('title').one()
    max_price = query_data[0]
    min_price = query_data[1]
    avg_price = float("%.1f" % query_data[2])
    left = int(min_price) - int(min_price) % 2
    right = int(max_price) + int(max_price) % 2
    resp_data = []
    for i in range(left, right, 2):
        data = get_price_area(i, i+2, brand)
        resp_data.append({
            'left': i,
            'right': i+2,
            'num': data[0][0] if len(data) else 0,
        })

    return resp_data, min_price, max_price, avg_price


def get_brand_score(brand):
    query_data = db.session.query(func.max(Shop.avgscore), func.min(Shop.avgscore), func.avg(Shop.avgscore)).filter(
        Shop.isMain == 1, Shop.record == 1, Shop.title == brand).group_by('title').one()
    max_score = query_data[0]
    min_score = query_data[1]
    avg_score = float("%.1f" % query_data[2])
    resp_data = []
    score = 0
    while score < 5:
        data = get_score_area(score, score+0.5, brand)
        resp_data.append({
            'left': score,
            'right': score + 0.5,
            'num': data[0][0] if len(data) else 0,
        })
        score += 0.5

    return resp_data, min_score, max_score, avg_score





