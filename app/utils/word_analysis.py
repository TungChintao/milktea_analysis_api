from sqlalchemy import func, distinct
from app.models import WordCloud
from app.libs.extensions import db


def get_all_word():
    query_data = db.session.query(WordCloud.keyword, func.count(WordCloud.keyword)).group_by('keyword').all()
    query_data.sort(key=lambda x: x[1], reverse=True)
    resp_data = []
    for i in range(50):
        resp_data.append({
            'name': query_data[i][0],
            'value': query_data[i][1]
        })
    return resp_data


def get_brand_word(brand):
    query_data = db.session.query(WordCloud.keyword, func.count(WordCloud.keyword)).filter(WordCloud.brand == brand).group_by('keyword').all()
    query_data.sort(key=lambda x: x[1], reverse=True)
    resp_data = []
    max_num = 35 if len(query_data) > 35 else len(query_data)
    for i in range(max_num):
        resp_data.append({
            'name': query_data[i][0],
            'value': query_data[i][1]
        })

    return resp_data
