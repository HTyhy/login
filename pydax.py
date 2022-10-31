_username = '2233'
_passwd = '114514'
new = 114514
username = input('请输入你的用户名: ')
passwd = input('请输入你的密码: ')
for i in range(1):
    if username == _username and passwd == _passwd:
        print('欢迎 %s 进入系统!' % _username)
        for i in range(10):
            _Answer = '1'
            Account = '2'
            print('抽奖系统“1”       个人账户“2”')
            Answer = input()
            if Answer == _Answer:
                for i in range(1):

                    a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                    if a == '进入':
                        import random


                        def lottery():
                            number = []
                            First_prize = []
                            Second_prize = []
                            Thire_prize = []
                            while len(set(number)) < 45:
                                number.append(random.randint(0, 100))
                                number = list(set(number))
                            while True:
                                if len(First_prize) < 10:
                                    First_prize.append(number.pop())
                                elif len(Second_prize) < 15:
                                    Second_prize.append(number.pop())
                                elif len(Thire_prize) < 20:
                                    Thire_prize.append(number.pop())
                                if len(First_prize) == 10 and len(Second_prize) == 15 and len(Thire_prize) == 20:
                                    break
                            return First_prize, Second_prize, Thire_prize


                        def main():
                            i = 0
                            first_count = 0
                            second_count = 0
                            third_count = 0
                            first = []
                            second = []
                            third = []
                            First_prize, Second_prize, Thire_prize = lottery()

                            while i < 3:
                                number = random.randint(0, 100)
                                if number in First_prize:
                                    first_count += 1
                                    first.append(number)
                                    First_prize.remove(number)
                                    print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                elif number in Second_prize:
                                    second_count += 1
                                    second.append(number)
                                    Second_prize.remove(number)
                                    print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                elif number in Thire_prize:
                                    third_count += 1
                                    third.append(number)
                                    Thire_prize.remove(number)
                                    print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                i += 1
                            print('一等奖中奖号码：', first)
                            print('二等奖中奖号码：', second)
                            print('三等奖中奖号码：', third)
                            key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                            if key == '是':
                                return main()
                            else:
                                print('游戏结束')


                        if __name__ == "__main__":
                            main()
                    else:
                        break
            print('抽奖系统“1”       个人账户“2”')
            Answer = input()
            if Answer == Account:
                print('你的账号：222')
                print('你的密码：233')
            else:
                for i in range(1):

                    a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                    if a == '进入':
                        import random


                        def lottery():
                            number = []
                            First_prize = []
                            Second_prize = []
                            Thire_prize = []
                            while len(set(number)) < 45:
                                number.append(random.randint(0, 100))
                                number = list(set(number))
                            while True:
                                if len(First_prize) < 10:
                                    First_prize.append(number.pop())
                                elif len(Second_prize) < 15:
                                    Second_prize.append(number.pop())
                                elif len(Thire_prize) < 20:
                                    Thire_prize.append(number.pop())
                                if len(First_prize) == 10 and len(Second_prize) == 15 and len(Thire_prize) == 20:
                                    break
                            return First_prize, Second_prize, Thire_prize


                        def main():
                            i = 0
                            first_count = 0
                            second_count = 0
                            third_count = 0
                            first = []
                            second = []
                            third = []
                            First_prize, Second_prize, Thire_prize = lottery()

                            while i < 3:
                                number = random.randint(0, 100)
                                if number in First_prize:
                                    first_count += 1
                                    first.append(number)
                                    First_prize.remove(number)
                                    print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                elif number in Second_prize:
                                    second_count += 1
                                    second.append(number)
                                    Second_prize.remove(number)
                                    print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                elif number in Thire_prize:
                                    third_count += 1
                                    third.append(number)
                                    Thire_prize.remove(number)
                                    print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                i += 1
                            print('一等奖中奖号码：', first)
                            print('二等奖中奖号码：', second)
                            print('三等奖中奖号码：', third)
                            key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                            if key == '是':
                                return main()
                            else:
                                print('游戏结束')


                        if __name__ == "__main__":
                            main()
                    else:
                        break

        break
    else:
        if username!=_username:
            print('你的用户名错了。')
            for i in range(1, 3):
                username = input('请输入你的用户名: ')
                passwd = input('请输入你的密码: ')
                if username == _username and passwd == _passwd:
                    print('欢迎 %s 进入系统!' % _username)
                    for i in range(10):
                        _Answer = '1'
                        Account = '2'
                        print('抽奖系统“1”       个人账户“2”')
                        Answer = input()

                        if Answer == _Answer:
                            for i in range(1):

                                a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                if a == '进入':
                                    import random


                                    def lottery():
                                        number = []
                                        First_prize = []
                                        Second_prize = []
                                        Thire_prize = []
                                        while len(set(number)) < 45:
                                            number.append(random.randint(0, 100))
                                            number = list(set(number))
                                        while True:
                                            if len(First_prize) < 10:
                                                First_prize.append(number.pop())
                                            elif len(Second_prize) < 15:
                                                Second_prize.append(number.pop())
                                            elif len(Thire_prize) < 20:
                                                Thire_prize.append(number.pop())
                                            if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                    Thire_prize) == 20:
                                                break
                                        return First_prize, Second_prize, Thire_prize


                                    def main():
                                        i = 0
                                        first_count = 0
                                        second_count = 0
                                        third_count = 0
                                        first = []
                                        second = []
                                        third = []
                                        First_prize, Second_prize, Thire_prize = lottery()

                                        while i < 3:
                                            number = random.randint(0, 100)
                                            if number in First_prize:
                                                first_count += 1
                                                first.append(number)
                                                First_prize.remove(number)
                                                print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                            elif number in Second_prize:
                                                second_count += 1
                                                second.append(number)
                                                Second_prize.remove(number)
                                                print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                            elif number in Thire_prize:
                                                third_count += 1
                                                third.append(number)
                                                Thire_prize.remove(number)
                                                print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                            i += 1
                                        print('一等奖中奖号码：', first)
                                        print('二等奖中奖号码：', second)
                                        print('三等奖中奖号码：', third)
                                        key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                        if key == '是':
                                            return main()
                                        else:
                                            print('游戏结束')


                                    if __name__ == "__main__":
                                        main()
                                else:
                                    break
                        print('抽奖系统“1”       个人账户“2”')
                        Answer = input()
                        if Answer == Account:
                            print('你的账号：222')
                            print('你的密码：233')
                        else:
                            for i in range(1):

                                a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                if a == '进入':
                                    import random


                                    def lottery():
                                        number = []
                                        First_prize = []
                                        Second_prize = []
                                        Thire_prize = []
                                        while len(set(number)) < 45:
                                            number.append(random.randint(0, 100))
                                            number = list(set(number))
                                        while True:
                                            if len(First_prize) < 10:
                                                First_prize.append(number.pop())
                                            elif len(Second_prize) < 15:
                                                Second_prize.append(number.pop())
                                            elif len(Thire_prize) < 20:
                                                Thire_prize.append(number.pop())
                                            if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                    Thire_prize) == 20:
                                                break
                                        return First_prize, Second_prize, Thire_prize


                                    def main():
                                        i = 0
                                        first_count = 0
                                        second_count = 0
                                        third_count = 0
                                        first = []
                                        second = []
                                        third = []
                                        First_prize, Second_prize, Thire_prize = lottery()

                                        while i < 3:
                                            number = random.randint(0, 100)
                                            if number in First_prize:
                                                first_count += 1
                                                first.append(number)
                                                First_prize.remove(number)
                                                print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                            elif number in Second_prize:
                                                second_count += 1
                                                second.append(number)
                                                Second_prize.remove(number)
                                                print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                            elif number in Thire_prize:
                                                third_count += 1
                                                third.append(number)
                                                Thire_prize.remove(number)
                                                print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                            i += 1
                                        print('一等奖中奖号码：', first)
                                        print('二等奖中奖号码：', second)
                                        print('三等奖中奖号码：', third)
                                        key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                        if key == '是':
                                            return main()
                                        else:
                                            print('游戏结束')


                                    if __name__ == "__main__":
                                        main()
                                else:
                                    break

                    break
                else:
                    if username != _username:
                        print('你的用户名错了。')
                    elif passwd != _passwd:
                        print('你的密码错了。')
                    else:
                        print('欢迎 %s 进入系统!')
                        for i in range(10):
                            _Answer = '1'
                            Account = '2'
                            print('抽奖系统“1”       个人账户“2”')
                            Answer = input()

                            if Answer == _Answer:
                                for i in range(1):

                                    a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                    if a == '进入':
                                        import random


                                        def lottery():
                                            number = []
                                            First_prize = []
                                            Second_prize = []
                                            Thire_prize = []
                                            while len(set(number)) < 45:
                                                number.append(random.randint(0, 100))
                                                number = list(set(number))
                                            while True:
                                                if len(First_prize) < 10:
                                                    First_prize.append(number.pop())
                                                elif len(Second_prize) < 15:
                                                    Second_prize.append(number.pop())
                                                elif len(Thire_prize) < 20:
                                                    Thire_prize.append(number.pop())
                                                if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                        Thire_prize) == 20:
                                                    break
                                            return First_prize, Second_prize, Thire_prize


                                        def main():
                                            i = 0
                                            first_count = 0
                                            second_count = 0
                                            third_count = 0
                                            first = []
                                            second = []
                                            third = []
                                            First_prize, Second_prize, Thire_prize = lottery()

                                            while i < 3:
                                                number = random.randint(0, 100)
                                                if number in First_prize:
                                                    first_count += 1
                                                    first.append(number)
                                                    First_prize.remove(number)
                                                    print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                                elif number in Second_prize:
                                                    second_count += 1
                                                    second.append(number)
                                                    Second_prize.remove(number)
                                                    print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                                elif number in Thire_prize:
                                                    third_count += 1
                                                    third.append(number)
                                                    Thire_prize.remove(number)
                                                    print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                                i += 1
                                            print('一等奖中奖号码：', first)
                                            print('二等奖中奖号码：', second)
                                            print('三等奖中奖号码：', third)
                                            key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                            if key == '是':
                                                return main()
                                            else:
                                                print('游戏结束')


                                        if __name__ == "__main__":
                                            main()
                                    else:
                                        break
                            print('抽奖系统“1”       个人账户“2”')
                            Answer = input()
                            if Answer == Account:
                                print('你的账号：222')
                                print('你的密码：233')
                            else:
                                for i in range(1):

                                    a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                    if a == '进入':
                                        import random


                                        def lottery():
                                            number = []
                                            First_prize = []
                                            Second_prize = []
                                            Thire_prize = []
                                            while len(set(number)) < 45:
                                                number.append(random.randint(0, 100))
                                                number = list(set(number))
                                            while True:
                                                if len(First_prize) < 10:
                                                    First_prize.append(number.pop())
                                                elif len(Second_prize) < 15:
                                                    Second_prize.append(number.pop())
                                                elif len(Thire_prize) < 20:
                                                    Thire_prize.append(number.pop())
                                                if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                        Thire_prize) == 20:
                                                    break
                                            return First_prize, Second_prize, Thire_prize


                                        def main():
                                            i = 0
                                            first_count = 0
                                            second_count = 0
                                            third_count = 0
                                            first = []
                                            second = []
                                            third = []
                                            First_prize, Second_prize, Thire_prize = lottery()

                                            while i < 3:
                                                number = random.randint(0, 100)
                                                if number in First_prize:
                                                    first_count += 1
                                                    first.append(number)
                                                    First_prize.remove(number)
                                                    print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                                elif number in Second_prize:
                                                    second_count += 1
                                                    second.append(number)
                                                    Second_prize.remove(number)
                                                    print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                                elif number in Thire_prize:
                                                    third_count += 1
                                                    third.append(number)
                                                    Thire_prize.remove(number)
                                                    print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                                i += 1
                                            print('一等奖中奖号码：', first)
                                            print('二等奖中奖号码：', second)
                                            print('三等奖中奖号码：', third)
                                            key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                            if key == '是':
                                                return main()
                                            else:
                                                print('游戏结束')


                                        if __name__ == "__main__":
                                            main()
                                    else:
                                        break

            else:
                print("你的密码或用户名错了，请稍后再试")
        elif passwd!=_passwd:
            print('你的密码错了。')
            for i in range(1, 3):
                username = input('请输入你的用户名: ')
                passwd = input('请输入你的密码: ')
                if username == _username and passwd == _passwd:
                    print('欢迎 %s 进入系统!' % _username)
                    for i in range(10):
                        _Answer = '1'
                        Account = '2'
                        print('抽奖系统“1”       个人账户“2”')
                        Answer = input()

                        if Answer == _Answer:
                            for i in range(1):

                                a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                if a == '进入':
                                    import random


                                    def lottery():
                                        number = []
                                        First_prize = []
                                        Second_prize = []
                                        Thire_prize = []
                                        while len(set(number)) < 45:
                                            number.append(random.randint(0, 100))
                                            number = list(set(number))
                                        while True:
                                            if len(First_prize) < 10:
                                                First_prize.append(number.pop())
                                            elif len(Second_prize) < 15:
                                                Second_prize.append(number.pop())
                                            elif len(Thire_prize) < 20:
                                                Thire_prize.append(number.pop())
                                            if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                    Thire_prize) == 20:
                                                break
                                        return First_prize, Second_prize, Thire_prize


                                    def main():
                                        i = 0
                                        first_count = 0
                                        second_count = 0
                                        third_count = 0
                                        first = []
                                        second = []
                                        third = []
                                        First_prize, Second_prize, Thire_prize = lottery()

                                        while i < 3:
                                            number = random.randint(0, 100)
                                            if number in First_prize:
                                                first_count += 1
                                                first.append(number)
                                                First_prize.remove(number)
                                                print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                            elif number in Second_prize:
                                                second_count += 1
                                                second.append(number)
                                                Second_prize.remove(number)
                                                print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                            elif number in Thire_prize:
                                                third_count += 1
                                                third.append(number)
                                                Thire_prize.remove(number)
                                                print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                            i += 1
                                        print('一等奖中奖号码：', first)
                                        print('二等奖中奖号码：', second)
                                        print('三等奖中奖号码：', third)
                                        key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                        if key == '是':
                                            return main()
                                        else:
                                            print('游戏结束')


                                    if __name__ == "__main__":
                                        main()
                                else:
                                    break
                        print('抽奖系统“1”       个人账户“2”')
                        Answer = input()
                        if Answer == Account:
                            print('你的账号：222')
                            print('你的密码：233')
                        else:
                            for i in range(1):

                                a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                if a == '进入':
                                    import random


                                    def lottery():
                                        number = []
                                        First_prize = []
                                        Second_prize = []
                                        Thire_prize = []
                                        while len(set(number)) < 45:
                                            number.append(random.randint(0, 100))
                                            number = list(set(number))
                                        while True:
                                            if len(First_prize) < 10:
                                                First_prize.append(number.pop())
                                            elif len(Second_prize) < 15:
                                                Second_prize.append(number.pop())
                                            elif len(Thire_prize) < 20:
                                                Thire_prize.append(number.pop())
                                            if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                    Thire_prize) == 20:
                                                break
                                        return First_prize, Second_prize, Thire_prize


                                    def main():
                                        i = 0
                                        first_count = 0
                                        second_count = 0
                                        third_count = 0
                                        first = []
                                        second = []
                                        third = []
                                        First_prize, Second_prize, Thire_prize = lottery()

                                        while i < 3:
                                            number = random.randint(0, 100)
                                            if number in First_prize:
                                                first_count += 1
                                                first.append(number)
                                                First_prize.remove(number)
                                                print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                            elif number in Second_prize:
                                                second_count += 1
                                                second.append(number)
                                                Second_prize.remove(number)
                                                print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                            elif number in Thire_prize:
                                                third_count += 1
                                                third.append(number)
                                                Thire_prize.remove(number)
                                                print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                            i += 1
                                        print('一等奖中奖号码：', first)
                                        print('二等奖中奖号码：', second)
                                        print('三等奖中奖号码：', third)
                                        key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                        if key == '是':
                                            return main()
                                        else:
                                            print('游戏结束')


                                    if __name__ == "__main__":
                                        main()
                                else:
                                    break

                    break
                else:
                    if username != _username:
                        print('你的用户名错了。')
                    elif passwd != _passwd:
                        print('你的密码错了。')
                    else:
                        print('欢迎 %s 进入系统!')
                        for i in range(10):
                            _Answer = '1'
                            Account = '2'
                            print('抽奖系统“1”       个人账户“2”')
                            Answer = input()

                            if Answer == _Answer:
                                for i in range(1):

                                    a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                    if a == '进入':
                                        import random


                                        def lottery():
                                            number = []
                                            First_prize = []
                                            Second_prize = []
                                            Thire_prize = []
                                            while len(set(number)) < 45:
                                                number.append(random.randint(0, 100))
                                                number = list(set(number))
                                            while True:
                                                if len(First_prize) < 10:
                                                    First_prize.append(number.pop())
                                                elif len(Second_prize) < 15:
                                                    Second_prize.append(number.pop())
                                                elif len(Thire_prize) < 20:
                                                    Thire_prize.append(number.pop())
                                                if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                        Thire_prize) == 20:
                                                    break
                                            return First_prize, Second_prize, Thire_prize


                                        def main():
                                            i = 0
                                            first_count = 0
                                            second_count = 0
                                            third_count = 0
                                            first = []
                                            second = []
                                            third = []
                                            First_prize, Second_prize, Thire_prize = lottery()

                                            while i < 3:
                                                number = random.randint(0, 100)
                                                if number in First_prize:
                                                    first_count += 1
                                                    first.append(number)
                                                    First_prize.remove(number)
                                                    print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                                elif number in Second_prize:
                                                    second_count += 1
                                                    second.append(number)
                                                    Second_prize.remove(number)
                                                    print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                                elif number in Thire_prize:
                                                    third_count += 1
                                                    third.append(number)
                                                    Thire_prize.remove(number)
                                                    print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                                i += 1
                                            print('一等奖中奖号码：', first)
                                            print('二等奖中奖号码：', second)
                                            print('三等奖中奖号码：', third)
                                            key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                            if key == '是':
                                                return main()
                                            else:
                                                print('游戏结束')


                                        if __name__ == "__main__":
                                            main()
                                    else:
                                        break
                            print('抽奖系统“1”       个人账户“2”')
                            Answer = input()
                            if Answer == Account:
                                print('你的账号：222')
                                print('你的密码：233')

            else:
                print("你的密码或用户名错了，请稍后再试")
        else:
            for i in range(1, 3):
                username = input('请输入你的用户名: ')
                passwd = input('请输入你的密码: ')
                if username == _username and passwd == _passwd:
                    print('欢迎 %s 进入系统!' % _username)
                    for i in range(10):
                        _Answer = '1'
                        Account = '2'
                        print('抽奖系统“1”       个人账户“2”')
                        Answer = input()

                        if Answer == _Answer:
                            for i in range(1):

                                a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                if a == '进入':
                                    import random


                                    def lottery():
                                        number = []
                                        First_prize = []
                                        Second_prize = []
                                        Thire_prize = []
                                        while len(set(number)) < 45:
                                            number.append(random.randint(0, 100))
                                            number = list(set(number))
                                        while True:
                                            if len(First_prize) < 10:
                                                First_prize.append(number.pop())
                                            elif len(Second_prize) < 15:
                                                Second_prize.append(number.pop())
                                            elif len(Thire_prize) < 20:
                                                Thire_prize.append(number.pop())
                                            if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                    Thire_prize) == 20:
                                                break
                                        return First_prize, Second_prize, Thire_prize


                                    def main():
                                        i = 0
                                        first_count = 0
                                        second_count = 0
                                        third_count = 0
                                        first = []
                                        second = []
                                        third = []
                                        First_prize, Second_prize, Thire_prize = lottery()

                                        while i < 3:
                                            number = random.randint(0, 100)
                                            if number in First_prize:
                                                first_count += 1
                                                first.append(number)
                                                First_prize.remove(number)
                                                print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                            elif number in Second_prize:
                                                second_count += 1
                                                second.append(number)
                                                Second_prize.remove(number)
                                                print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                            elif number in Thire_prize:
                                                third_count += 1
                                                third.append(number)
                                                Thire_prize.remove(number)
                                                print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                            i += 1
                                        print('一等奖中奖号码：', first)
                                        print('二等奖中奖号码：', second)
                                        print('三等奖中奖号码：', third)
                                        key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                        if key == '是':
                                            return main()
                                        else:
                                            print('游戏结束')


                                    if __name__ == "__main__":
                                        main()
                                else:
                                    break
                        print('抽奖系统“1”       个人账户“2”')
                        Answer = input()
                        if Answer == Account:
                            print('你的账号：222')
                            print('你的密码：233')
                        else:
                            for i in range(1):

                                a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                if a == '进入':
                                    import random


                                    def lottery():
                                        number = []
                                        First_prize = []
                                        Second_prize = []
                                        Thire_prize = []
                                        while len(set(number)) < 45:
                                            number.append(random.randint(0, 100))
                                            number = list(set(number))
                                        while True:
                                            if len(First_prize) < 10:
                                                First_prize.append(number.pop())
                                            elif len(Second_prize) < 15:
                                                Second_prize.append(number.pop())
                                            elif len(Thire_prize) < 20:
                                                Thire_prize.append(number.pop())
                                            if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                    Thire_prize) == 20:
                                                break
                                        return First_prize, Second_prize, Thire_prize


                                    def main():
                                        i = 0
                                        first_count = 0
                                        second_count = 0
                                        third_count = 0
                                        first = []
                                        second = []
                                        third = []
                                        First_prize, Second_prize, Thire_prize = lottery()

                                        while i < 3:
                                            number = random.randint(0, 100)
                                            if number in First_prize:
                                                first_count += 1
                                                first.append(number)
                                                First_prize.remove(number)
                                                print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                            elif number in Second_prize:
                                                second_count += 1
                                                second.append(number)
                                                Second_prize.remove(number)
                                                print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                            elif number in Thire_prize:
                                                third_count += 1
                                                third.append(number)
                                                Thire_prize.remove(number)
                                                print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                            i += 1
                                        print('一等奖中奖号码：', first)
                                        print('二等奖中奖号码：', second)
                                        print('三等奖中奖号码：', third)
                                        key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                        if key == '是':
                                            return main()
                                        else:
                                            print('游戏结束')


                                    if __name__ == "__main__":
                                        main()
                                else:
                                    break

                    break
                else:
                    if username != _username:
                        print('你的用户名错了。')
                    elif passwd != _passwd:
                        print('你的密码错了。')
                    else:
                        print('欢迎 %s 进入系统!')
                        for i in range(10):
                            _Answer = '1'
                            Account = '2'
                            print('抽奖系统“1”       个人账户“2”')
                            Answer = input()


                            if Answer == _Answer:
                                for i in range(1):

                                    a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                    if a == '进入':
                                        import random


                                        def lottery():
                                            number = []
                                            First_prize = []
                                            Second_prize = []
                                            Thire_prize = []
                                            while len(set(number)) < 45:
                                                number.append(random.randint(0, 100))
                                                number = list(set(number))
                                            while True:
                                                if len(First_prize) < 10:
                                                    First_prize.append(number.pop())
                                                elif len(Second_prize) < 15:
                                                    Second_prize.append(number.pop())
                                                elif len(Thire_prize) < 20:
                                                    Thire_prize.append(number.pop())
                                                if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                        Thire_prize) == 20:
                                                    break
                                            return First_prize, Second_prize, Thire_prize


                                        def main():
                                            i = 0
                                            first_count = 0
                                            second_count = 0
                                            third_count = 0
                                            first = []
                                            second = []
                                            third = []
                                            First_prize, Second_prize, Thire_prize = lottery()

                                            while i < 3:
                                                number = random.randint(0, 100)
                                                if number in First_prize:
                                                    first_count += 1
                                                    first.append(number)
                                                    First_prize.remove(number)
                                                    print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                                elif number in Second_prize:
                                                    second_count += 1
                                                    second.append(number)
                                                    Second_prize.remove(number)
                                                    print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                                elif number in Thire_prize:
                                                    third_count += 1
                                                    third.append(number)
                                                    Thire_prize.remove(number)
                                                    print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                                i += 1
                                            print('一等奖中奖号码：', first)
                                            print('二等奖中奖号码：', second)
                                            print('三等奖中奖号码：', third)
                                            key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                            if key == '是':
                                                return main()
                                            else:
                                                print('游戏结束')


                                        if __name__ == "__main__":
                                            main()
                                    else:
                                        break
                            print('抽奖系统“1”       个人账户“2”')
                            Answer = input()
                            if Answer == Account:
                                print('你的账号：222')
                                print('你的密码：233')
                            else:
                                for i in range(1):

                                    a = input('欢迎进入抽奖机v1.0，进入抽奖机请输入“进入”：')
                                    if a == '进入':
                                        import random


                                        def lottery():
                                            number = []
                                            First_prize = []
                                            Second_prize = []
                                            Thire_prize = []
                                            while len(set(number)) < 45:
                                                number.append(random.randint(0, 100))
                                                number = list(set(number))
                                            while True:
                                                if len(First_prize) < 10:
                                                    First_prize.append(number.pop())
                                                elif len(Second_prize) < 15:
                                                    Second_prize.append(number.pop())
                                                elif len(Thire_prize) < 20:
                                                    Thire_prize.append(number.pop())
                                                if len(First_prize) == 10 and len(Second_prize) == 15 and len(
                                                        Thire_prize) == 20:
                                                    break
                                            return First_prize, Second_prize, Thire_prize


                                        def main():
                                            i = 0
                                            first_count = 0
                                            second_count = 0
                                            third_count = 0
                                            first = []
                                            second = []
                                            third = []
                                            First_prize, Second_prize, Thire_prize = lottery()

                                            while i < 3:
                                                number = random.randint(0, 100)
                                                if number in First_prize:
                                                    first_count += 1
                                                    first.append(number)
                                                    First_prize.remove(number)
                                                    print("恭喜您，第{}次中一等奖，中奖号码是：{}".format(first_count, number))
                                                elif number in Second_prize:
                                                    second_count += 1
                                                    second.append(number)
                                                    Second_prize.remove(number)
                                                    print("恭喜您，第{}次中二等奖，中奖号码是：{}".format(second_count, number))
                                                elif number in Thire_prize:
                                                    third_count += 1
                                                    third.append(number)
                                                    Thire_prize.remove(number)
                                                    print("恭喜您，第{}次中三等奖，中奖号码是：{}".format(third_count, number))
                                                i += 1
                                            print('一等奖中奖号码：', first)
                                            print('二等奖中奖号码：', second)
                                            print('三等奖中奖号码：', third)
                                            key = input('抽奖结束，输入"是"进行一轮新的抽奖：')
                                            if key == '是':
                                                return main()
                                            else:
                                                print('游戏结束')


                                        if __name__ == "__main__":
                                            main()
                                    else:
                                        break



            else:
                print("你的密码或用户名错了，请稍后再试")



