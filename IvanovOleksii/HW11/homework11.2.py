def main(num: int):
    try:
        if not isinstance(num, int):
            raise Exception('Enter the number!!!')

        if num < 0:
            raise Exception('enter the number corresponding to the day of the week')
        elif num > 7:
            raise Exception('enter the number corresponding to the day of the week')

        match num:
            case 1:
                return 'Monday'
            case 2:
                return 'Tuesday'
            case 3:
                return 'Wednesday'
            case 4:
                return 'Thursday'
            case 5:
                return 'Friday'
            case 6:
                return 'Saturday'
            case 7:
                return 'Sunday'
    except Exception as e:
        return e


if __name__ == '__main__':
    print(main(0))
