

if __name__ == "__main__":

    from simple_unittest import simple_unittest_function

    cat = 4
    mouse = 2

    test_conditions = [
                            ("cat == mouse + mouse", cat, mouse + mouse),
                            ("cat == mouse", cat, mouse),
                            ("cat == 4", cat, 4)
                        ]
    

    for each in test_conditions:
        simple_unittest_function(*each)

