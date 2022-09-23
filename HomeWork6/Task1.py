# Мимикрия

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation = lambda x: x

transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('Равны')
else:
    print('Не равны!')
