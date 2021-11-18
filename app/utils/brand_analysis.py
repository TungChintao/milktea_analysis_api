from sqlalchemy import func, distinct
from app.models import Shop, Good
from app.libs.extensions import db


def get_brand_detail(brand):
    query_data = db.session.query(Shop.city, Shop.avgprice, func.count(Shop.title)).filter(Shop.title == brand).group_by('city').all()
    resp_data = []
    city_num = 0
    for data in query_data:
        city_num += 1
        resp_data.append({
            'city': data[0],
            'avgprice': data[1],
            'shopnum': data[2],
        })
    return city_num, resp_data


def get_price_area(left, right, brand):
    query_data = db.session.query(func.count(Shop.shopid)).filter(Shop.title == brand, Shop.avgprice >= left, Shop.avgprice <= right).group_by('title').all()
    return query_data


def get_score_area(left, right, brand):
    query_data = db.session.query(func.count(Shop.shopid)).filter(Shop.title == brand, Shop.avgscore >= left, Shop.avgscore <= right).group_by('title').all()
    print(query_data)
    return query_data


def get_brand_price(brand):
    query_data = db.session.query(func.max(Shop.avgprice), func.min(Shop.avgprice)).filter(Shop.isMain == 1, Shop.record == 1,Shop.title == brand).group_by('title').one()
    max_price = int(query_data[0])
    min_price = int(query_data[1])
    resp_data = []
    for i in range(min_price, max_price, 2):
        data = get_price_area(i, i+2, brand)
        resp_data.append({
            'left': i,
            'right': i+2,
            'num': data[0][0],
        })

    return resp_data


def get_brand_score(brand):
    resp_data = []
    score = 0
    while score < 5:
        print(score)
        data = get_score_area(score, score+0.5, brand)
        resp_data.append({
            'left': score,
            'right': score + 0.5,
            'num': data[0][0] if len(data) else 0,
        })
        score += 0.5

    return resp_data






