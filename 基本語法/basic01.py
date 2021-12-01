if __name__ == '__main__':
    print(__name__)
    h = 170
    w = 60.0
    print(h, w)
    print(type(h), type(w))
    bmi = w / ((h/100)**2)
    print('bmi=', bmi)
    print('bmi=' + str(bmi))
    print('bmi=%.2f' % bmi)
    print('bmi={0}'.format(bmi))
    print(f'bmi={bmi}')