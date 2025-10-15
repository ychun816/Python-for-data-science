from ft_package import count_in_list

if __name__ == '__main__':
    test_list = ["toto", "tata", "toto"]
    print(count_in_list(test_list, "toto"))  # expected: 2
    print(count_in_list(test_list, "tutu"))  # expected: 0
