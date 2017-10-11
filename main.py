"""Main app file"""
import linear
import format_math


def read():
    user_input = raw_input('$->')

    if user_input.upper() == 'QUIT':
        return 0
    try:
        coordinates = extract_values(user_input)
        equation = linear.calc_equation(coordinates)
        print '\n' + format_math.equation(equation) + '\n'
    except ValueError:
        print 'invalid input!'
    read()


def extract_values(user_input):
    values = user_input.strip(' ').split(' ')
    coordinate1 = {'x': int(values[0]), 'y': int(values[1])}
    coordinate2 = {'x': int(values[2]), 'y': int(values[3])}
    return [coordinate1, coordinate2]


def print_app_info():
    print '\nType 2 coordenates to get linear equation. (x1, y1, x2, y2)'
    print 'Type "quit" do stop\n'


def main():
    print_app_info()
    read()


if __name__ == "__main__":
    main()
