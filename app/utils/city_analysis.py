from app.models import Shop


# 获取35个城市列表
def get_cities_list():
    city_list = []
    results = Shop.query.all()
    for i in results:
        if i.city not in city_list:
            city_list.append(i.city)
    return city_list


# 获取该城市中的主要品牌
def get_title_list(city_name):
    title_list = []
    # 获取数据库中该城市的所有品牌的元组
    shops = Shop.query.filter(Shop.city == city_name, Shop.isMain == 1)
    for shop in shops:
        get_title = shop.title
        if get_title not in title_list:
            title_list.append(get_title)
    return title_list


# 获取该城市主要品牌的店铺数量列表
def get_title_num_list(city_name):
    titltnum_list = []
    shops = Shop.query.filter(Shop.isMain == 1).filter_by(city=city_name)
    t_list = get_title_list(city_name)
    for t in t_list:
        num = shops.filter(Shop.title == t).count()
        titltnum_list.append(num)
    return titltnum_list


# 获取该城市前五十的品牌及店铺数量列表
def get_fifty_shops(city_name):
    title_list = get_title_list(city_name)
    title_num_list = get_title_num_list(city_name)
    title_dict = dict(zip(title_list, title_num_list))
    a = sorted(title_dict.items(), key=lambda x: x[1], reverse=True)
    result = []
    for n in range(50):
        result.append(a[n])
    return result


# 获取该城市前50品牌在35个城市中的数量占比
def get_percentage(city_name):
    a = get_fifty_shops(city_name)
    percentage_list = []
    for n in range(50):
        t = a[n][0]
        num = Shop.query.filter(Shop.title == t, Shop.isMain == 1).count()
        p = a[n][1]/num
        p = "%.2f" % p
        percentage_list.append(p)
    return percentage_list


# 获取城市地图中店铺散点图信息
def shop_details(city_name):
    json_list = []
    # 获取数据库中该城市的所有店铺的元组
    shops = Shop.query.filter(Shop.city == city_name, Shop.isMain == 1, Shop.avgprice > 0)
    # 遍历所有元组，获取（店铺名称、经纬度、所在区域、人均消费）等信息，并整理成字典，把该字典插入data列表中
    for shop in shops:
        get_title = shop.title
        get_latitude = shop.latitude
        get_longitude = shop.longitude
        get_avgprice = "%.2f" % shop.avgprice
        get_address = shop.address
        shop1 = {
            'title': get_title,
            'latitude': get_latitude,
            'longitude': get_longitude,
            'avgprice': get_avgprice,
            'address': get_address
        }
        json_list.append(shop1)
    return json_list


# 获取前五品牌的名称列表
def get_five_shops(city_name):
    title_list = get_title_list(city_name)
    title_num_list = get_title_num_list(city_name)
    title_dict = dict(zip(title_list, title_num_list))
    a = sorted(title_dict.items(), key=lambda x: x[1], reverse=True)
    result = []
    for n in range(5):
        result.append(a[n][0])
    return result


# 获取前五品牌的所在区域列表
def fiveshops_address(city_name):
    titles = get_five_shops(city_name)
    address_list = []
    for t in titles:
        shops = Shop.query.filter_by(city=city_name, title=t, isMain=1)
        for shop in shops:
            if shop.address not in address_list:
                address_list.append(shop.address)
    return address_list


# 获取各个品牌的店铺数量在各个区域的列表
def get_fiveshops_num(city_name, title, address):
    list2 = []
    for a in address:
        list1 = []
        shops = Shop.query.filter_by(city=city_name, address=a, isMain=1)
        for t in title:
            num = shops.filter_by(title=t).count()
            list1.append(num)
        list2.append(list1)
    return list2
