# a UTF-8 encoded fille
# path = "./lorum.txt"


    # In [13]: with open("./lorum.txt", mode="r") as fille:
    # ...:     y = set()
    # ...:     for y in fille:
    # ...:         print(y)
    # ...:     print(f'we have a list of {set(y) for y in fille}')


def make_dict(path="./lorum.txt"):
    with open(path, mode="r") as fille:
        arr = fille.read()
        arr_new = arr.translate({ord(','):None}).translate({ord('.'):None})
        result = {} 
        for i, word in enumerate(arr_new.split()):
            result[i] = word.title() 
            print(f"{i + 1} : {word.title()}") 
        # print(result)

    """
    This function will take an fille.
    And write it out out as an Dictonary.
    """
    return result


def make_dict_and_write(path="./random.txt", path_w="./new.txt"):
    with open(path, mode="r") as file:
        arr = file.read()
        arr_new = arr.translate({ord(','):None}).translate({ord('.'):None})
        result = {0 : ""} 
        print(arr_new)
        try:
            with open(path_w, mode="r") as test_read:
                if (len(test_read.read()) > 2):
                    q = input("-- The fille isn't empy do you wish to overwerite? yes or no: ")
                    if (q == 'yes'):
                        open(path_w, mode="w").close()
                        for i, word in enumerate(arr_new.split()):
                            with open(path_w, mode="a") as write_file:
                                write_file.write(f"{i} : {word.title()},\n")
                                print(f"{i + 1} : {word.title()}")
                        return result
                    else:
                        print("--! not writing anything")
                        return
                else:
                    print("printing to fille")
                    for i, word in enumerate(arr_new.split()):
                        with open(path_w, mode="a") as write_file:
                            write_file.write(f"{i} : {word.title()},\n")
                            print(f"{i + 1} : {word.title()}")
                    return result
        except:
            print("an error has accourd")
    """
    This function will take an fille.
    And write it out out as an Dictonary.
    """
    # return result


# def print_dict(self):
    # for i, word in result:
        # print(f"{i} : {word.title()}")


def main() -> None:
    make_dict_and_write()
    # make_dict()
    # test = make_dict("./random.txt", "./new.txt")
    # print(test)


if __name__ == "__main__":
    main()
