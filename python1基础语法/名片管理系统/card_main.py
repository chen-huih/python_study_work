import card_function

if __name__ == '__main__':

    while True:
        user_action = card_function.menu()
        action = input("请选择您的操作：")
        if action in ('1', '2', '3'):
            if action == '1':
                card_function.add_user()
            elif action == '2':
                card_function.showal_user()
            else:
                card_function.check_user()
        elif action == 0:
            break
        else:
            print("输入违规！")
