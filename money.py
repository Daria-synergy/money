import csv
import datetime
class Goal:
    def __init__(self):
        self.l = []
        with open('goals.csv', 'r') as file:
            fieldnames = ['Цель', 'Итоговая сумма', 'Баланс', 'Категория', 'Статус', 'Последнее изменение']
            reader = csv.DictReader(file, fieldnames=fieldnames)
            for row in reader:
                self.l.append(row)
    def add(self, goal, sum_, balance, cat):
        g = {}
        g['Цель'] = goal
        g['Итоговая сумма'] = int(sum_)
        g['Баланс'] = int(balance)
        g['Категория'] = cat
        g['Статус'] = 'Не выполнена'
        g['Последнее изменение'] = str(datetime.date.today())
        self.l.append(g)
    def save_(self):
        with open('goals.csv', 'w') as file:
            fieldnames = ['Цель', 'Итоговая сумма', 'Баланс', 'Категория', 'Статус', 'Последнее изменение']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for i in self.l:
                writer.writerow(i)
    def del1(self, n):
        self.l.pop(n)
    def balplus(self, c, n):
        self.l[c]['Баланс'] = str(int(self.l[c]['Баланс']) + n)
        if int(self.l[c]['Баланс'])>= int(self.l[c]['Итоговая сумма']):
            self.l[c]['Баланс'] = self.l[c]['Итоговая сумма']
            print('Цель выполнена!')
            self.l[c]['Статус'] = 'Выполнена'
        elif int(self.l[c]['Баланс']) >= int(int(self.l[c]['Итоговая сумма']) / 2):
            print('Поздравляем! Вы достигли половины цели!')
    def balmin(self, c, n):
        self.l[c]['Баланс'] = str(int(self.l[c]['Баланс']) - n)
        if int(self.l[c]['Баланс']) < 0:
            self.l[c]['Баланс'] = '0'
    def inf(self):
        c1 = 0
        c2 = 0
        sum_bal = 0
        sum_it = 0
        for i in range(len(self.l)):
            print(f"{i + 1} накопление")
            for j in self.l[i]:
                print(f"{j}: {self.l[i][j]}")
            print(f"Процент выполнения цели: {int(int(self.l[i]['Баланс']) / int(self.l[i]['Итоговая сумма']) * 100)}%")
            sum_bal += int(self.l[i]['Баланс'])
            sum_it += int(self.l[i]['Итоговая сумма'])
            if self.l[i]['Статус'] =='Выполнена':
                c1 += 1
            elif self.l[i]['Статус'] =='Не выполнена':
                c2 += 1
            print('')
        try:
            print(f"Общий прогресс: {int(sum_bal / sum_it * 100)}%")
            print(f"Выполненные цели: {c1}")
            print(f"Невыполненные цели: {c2}")
        except ZeroDivisionError:
            print('')

g = Goal()
print('Добро пожаловать!')
def menu():
    global g
    print('Выберите нужное действие')
    print('1) Добавить новую цель;')
    print('2) Просмотр и изменение информации о всех целях;')
    print('3) Выход из программы.')
    a = input()
    num = ['1', '2', '3']
    if not a in num:
        print('Некорректный ввод. Вы можете ввести только число, соответствующее нужной команде.')
        print('')
        return menu()
    else:
        if a == '1':
            goal = input('Назовите цель ')
            bool1 = False
            while not bool1:
                try:
                    sum_ = int(input('Назовите итоговую сумму '))
                    if sum_ <= 0:
                        print('Итоговая сумма не может быть меньше либо равной нулю.')
                        continue
                    else:
                        bool1 = True
                except ValueError:
                    print('Вы можете ввести только целое числовое значение.')
                    continue
            bool2 = False
            while not bool2:
                try:
                    balance = int(input('Назовите баланс '))
                    if balance < 0:
                        print('Баланс не может быть меньше нуля.')
                        continue
                    elif balance >= sum_:
                        print('Баланс не может быть больше либо равным итоговой сумме.')
                        continue
                    else:
                        bool2 = True
                except ValueError:
                    print('Вы можете ввести только целое числовое значение.')
                    continue
            bool3 = False
            while not bool3:
                try:
                    print('Выберите категорию')
                    print('1) Хобби;')
                    print('2) Здоровье;')
                    print('3) Работа;')
                    print('4) Образование;')
                    print('5) Прочее.')
                    k1 = int(input())
                    num = [1, 2, 3, 4, 5]
                    if not k1 in num:
                        print('Некорректный ввод. Вы можете ввести только число, соответствующее нужному накоплению.')
                        continue
                    else:
                        if k1 == 1:
                            cat = 'Хобби'
                        elif k1 == 2:
                            cat = 'Здоровье'
                        elif k1 == 3:
                            cat = 'Работа'
                        elif k1 == 4:
                            cat = 'Образование'
                        elif k1 == 5:
                            cat = 'Прочее'
                        bool3 = True
                except ValueError:
                    print('Вы можете ввести только целое числовое значение.')
                    continue

            g.add(goal, sum_, balance, cat)
            print('Цель успешно добавлена!')
            print('')
            return menu()
        elif a == '2':
            def inf1():
                global g
                g.inf()
                if len(g.l) == 0:
                    print('У вас пока нет накоплений!')
                    print('')
                    return menu()
                else:
                    print('С каким накоплением вы хотите работать?')
                try:
                    c = int(input())
                    if c > len(g.l) or c <= 0:
                        print('Некорректный ввод. Вы можете ввести только число, соответствующее нужному накоплению.')
                        print('')
                        return inf1()
                    else:
                        for i in g.l[c - 1]:
                            print(f"{i}: {g.l[c - 1][i]}")
                        print(f"Процент выполнения цели: {int(int(g.l[c - 1]['Баланс']) / int(g.l[c - 1]['Итоговая сумма']) * 100)}%")
                        def capital():
                            nonlocal c
                            global g
                            t = datetime.datetime.strptime(g.l[c - 1]['Последнее изменение'], "%Y-%m-%d")
                            if (datetime.datetime.today() - t).days > 30:
                                print('Вы не вносили изменения в баланс больше месяца!')
                            print('Выберите нужное действие')
                            print('1) Изменить баланс;')
                            print('2) Редактировать данные накопления;')
                            print('3) Удалить накопление;')
                            print('4) Отмена;')
                            print('5) Выйти в главное меню.')
                            num = ['1', '2', '3', '4', '5']
                            d = input()
                            if not d in num:
                                print('Некорректный ввод. Вы можете ввести только число, соответствующее нужной команде.')
                                print('')
                                return capital()
                            else:
                                if d == '4':
                                    print('')
                                    return inf1()
                                elif d == '1':
                                    def bal():
                                        nonlocal c
                                        global g
                                        print('Как вы желаете изменить баланс?')
                                        print('1) Увеличить;')
                                        print('2) Уменьшить;')
                                        print('3) Выйти в основное меню;')
                                        f = input()
                                        num = ['1', '2', '3']
                                        if not f in num:
                                            print('Некорректный ввод. Вы можете ввести только число, соответствующее нужной команде.')
                                            print('')
                                            return bal()
                                        else:
                                            if f == '3':
                                                print('')
                                                return menu()
                                            elif f == '1':
                                                print('Насколько вы желаете увеличить баланс?')
                                                try:
                                                    n1 = int(input())
                                                    if n1 <= 0:
                                                        print('Вы можете ввести только положительное число.')
                                                        print('')
                                                        return bal()
                                                    else:
                                                        g.balplus(c - 1, n1)
                                                        g.l[c - 1]['Последнее изменение'] = str(datetime.date.today())
                                                        print('Баланс успешно изменён!')
                                                        print('')
                                                        return menu()
                                                except ValueError:
                                                    print('Вы можете ввести только целое числовое значение.')
                                                    print('')
                                                    return bal()
                                            elif f == '2':
                                                print('Насколько вы желаете уменьшить баланс?')
                                                try:
                                                    n1 = int(input())
                                                    if n1 <= 0:
                                                        print('Вы можете ввести только положительное число.')
                                                        print('')
                                                        return bal()
                                                    else:
                                                        g.balmin(c - 1, n1)
                                                        g.l[c - 1]['Последнее изменение'] = str(datetime.date.today())
                                                        print('Баланс успешно изменён!')
                                                        print('')
                                                        return menu()
                                                except ValueError:
                                                    print('Вы можете ввести только целое числовое значение.')
                                                    print('')
                                                    return bal()
                                    bal()
                                elif d == '2':
                                    for i in g.l[c - 1]:
                                        print(f"{i}: {g.l[c - 1][i]}")
                                    print('Введите новые значения.')
                                    g.l[c - 1]['Цель'] = input('Назовите цель ')
                                    bool1 = False
                                    while not bool1:
                                        try:
                                            sum_ = int(input('Назовите итоговую сумму '))
                                            if sum_ <= 0:
                                                print('Итоговая сумма не может быть меньше либо равной нулю.')
                                                continue
                                            else:
                                                bool1 = True
                                        except ValueError:
                                            print('Вы можете ввести только целое числовое значение.')
                                            continue
                                    g.l[c - 1]['Итоговая сумма'] = sum_
                                    bool2 = False
                                    while not bool2:
                                        try:
                                            balance = int(input('Назовите баланс '))
                                            if balance < 0:
                                                print('Баланс не может быть меньше нуля.')
                                                continue
                                            elif balance >= sum_:
                                                print('Баланс не может быть больше либо равным итоговой сумме.')
                                                continue
                                            else:
                                                bool2 = True
                                        except ValueError:
                                            print('Вы можете ввести только целое числовое значение.')
                                            continue
                                    g.l[c - 1]['Баланс'] = balance
                                    bool3 = False
                                    while not bool3:
                                        try:
                                            print('Выберите категорию')
                                            print('1) Хобби;')
                                            print('2) Здоровье;')
                                            print('3) Работа;')
                                            print('4) Образование;')
                                            print('5) Прочее.')
                                            k1 = int(input())
                                            num = [1, 2, 3, 4, 5]
                                            if not k1 in num:
                                                print('Некорректный ввод. Вы можете ввести только число, соответствующее нужному накоплению.')
                                                continue
                                            else:
                                                if k1 == 1:
                                                    cat = 'Хобби'
                                                elif k1 == 2:
                                                    cat = 'Здоровье'
                                                elif k1 == 3:
                                                    cat = 'Работа'
                                                elif k1 == 4:
                                                    cat = 'Образование'
                                                elif k1 == 5:
                                                    cat = 'Прочее'
                                                bool3 = True
                                        except ValueError:
                                            print('Вы можете ввести только целое числовое значение.')
                                            continue
                                    g.l[c - 1]['Категория'] = cat
                                    g.l[c - 1]['Последнее изменение'] = str(datetime.date.today())
                                    print('Данные изменены.')
                                    print('')
                                    return menu()
                                elif d == '5':
                                    print('')
                                    return menu()
                                elif d == '3':
                                    def del_():
                                        print('Удалить накопление?')
                                        print('1) Да;')
                                        print('2) Нет.')
                                        e = input()
                                        num = ['1', '2']
                                        if not e in num:
                                            print('Некорректный ввод. Вы можете ввести только число, соответствующее нужной команде.')
                                            print('')
                                            return del_()
                                        else:
                                            if e == '2':
                                                return inf1()
                                            elif e == '1':
                                                g.del1(c - 1)
                                                print('Удаление успешно завершено!')
                                                print('')
                                                return menu()
                                    return del_()
                        return capital()
                except ValueError:
                    print('Некорректный ввод. Вы можете ввести только число, соответствующее нужному накоплению.')
                    print('')
                    return inf1()
            inf1()
        elif a == '3':
            def ex():
                global g
                num = ['1', '2']
                print('Желаете сохранить изменения?')
                print('1) Сохранить и выйти')
                print('2) Выйти без сохранения')
                b = input()
                if not b in num:
                    print('Некорректный ввод. Вы можете ввести только число, соответствующее нужной команде.')
                    print('')
                    return ex()
                if b == '1':
                    g.save_()
                    print('Все изменения сохранены. До свидания!')
                elif b == '2':
                    print('Изменения не сохранены. До свидания!')
            return ex()
menu()




