def split_booty(*purses):
    total_ingots = sum(purse.get('gold_ingots', 0) for purse in purses)
    base_ingots = total_ingots // 3
    remainder = total_ingots % 3

    purse1 = {'gold_ingots': base_ingots}
    purse2 = {'gold_ingots': base_ingots}
    purse3 = {'gold_ingots': base_ingots}

    if remainder == 1:
        purse1['gold_ingots'] += 1
    elif remainder == 2:
        purse1['gold_ingots'] += 1
        purse2['gold_ingots'] += 1

    print(purse1, purse2, purse3)

split_booty({'gold_ingots': 3}, {'gold_ingots': 2}, {'apples': 10})