#!/usr/bin/env python

from collections import namedtuple


def main():
    City = namedtuple("City", "name counrty population coordinates")
    tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))

    print(tokyo)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo[1])

    print(City._fields)

    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data)
    print(delhi._asdict())
    for key, value in delhi._asdict().items():
        print(key + ':', value)
    return 1


if __name__ == "__main__":
    main()
