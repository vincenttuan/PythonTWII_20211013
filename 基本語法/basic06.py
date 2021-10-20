"""
雞兔同籠
雞加兔子共有 83 隻，雞的腳加上兔子的腳共有 240 隻腳，求雞與兔子各有幾隻?
"""
if __name__ == '__main__':
    amount = 200
    feet = 240

    if amount * 2 <= feet <= amount * 4:
        rabbit = (feet - amount * 2)/(4-2)
        chicken = amount - rabbit
        print('兔子:', rabbit, "雞:", chicken)
    else:
        print('amount:', amount, 'feet:', feet, '設定不正確')
