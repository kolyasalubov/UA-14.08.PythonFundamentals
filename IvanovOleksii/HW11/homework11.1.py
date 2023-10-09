def main(age: int):
    try:
        if age < 0:
            raise Exception('age must be greater than zero!')
        if age % 2 == 0:
            return 'Your age is even'
        elif age % 2 != 0:
            return 'Your age is odd'
    except Exception as e:
        return e


if __name__ == '__main__':
    print(main(-4))
