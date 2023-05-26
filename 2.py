import random

# 定义一些常用的城市名词库
nouns = ['山', '江', '海', '城', '都', '州', '市', '港', '岛', '谷', '湖', '河', '镇', '村']
adjectives = ['新', '美', '大', '小', '东', '南', '西', '北', '青', '红', '白', '黄', '紫', '金', '银']

# 生成随机城市名
def generate_city_name():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return adjective + noun

# 生成多个随机城市名
def generate_random_cities(num_cities):
    cities = []
    for _ in range(num_cities):
        city_name = generate_city_name()
        cities.append(city_name)
    return cities

# 示例用法
random_cities = generate_random_cities(10)
for city in random_cities:
    print(city)

pip install -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/ pygame
