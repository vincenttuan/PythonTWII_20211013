def getRabbitAndChicken(amount, feet):
    rabbit = (feet - amount * 2)/(4-2)
    chicken = amount - rabbit
    return rabbit, chicken


if __name__ == '__main__':
    ra, ch = getRabbitAndChicken(83, 240)
    print(ra, ch)

    


