import collections


Rating = collections.namedtuple("Rating", "id, x, y, rating")




def main():
    for d in get_data_tricky():
        print("id={}, rating={}, position=({}, {})".format(d.id, d.rating, d.x, d.y))

    _, _ , x, y = d
    print(x,y)

def get_data_tricky():
    data = [

        Rating(1,19.2,11.1,50),
        Rating(2,18.9,12.0,45),
        Rating(3,20.1,140,55),
    ]

    return data


if __name__ == '__main__':
    main()