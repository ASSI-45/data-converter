# a UTF-8 encoded fille
# path = "./lorum.txt"


    # In [13]: with open("./lorum.txt", mode="r") as fille:
    # ...:     y = set()
    # ...:     for y in fille:
    # ...:         print(y)
    # ...:     print(f'we have a list of {set(y) for y in fille}')


def make_dict(path="./lorum.txt"):
    with open(path, mode="r") as fille:
        string = fille.read()
        new_stiring = string.translate({ord(','):None}).translate({ord('.'):None})
        result = {} 
        for i, word in enumerate(new_stiring.split()):
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
        string = file.read()  # puts the fille into a string type 
        # cleans it up 
        new_string = string.translate({ord(','):None}).translate({ord('.'):None})
        result = {0 : ""} # creates a dictonary 
        print(new_string)
        try:
            with open(path_w, mode="r") as test_read:
                if (len(test_read.read()) > 2):  # testing if the fille is empty
                    q = input("-- The fille isn't empy do you wish to overwerite? yes or no: ")
                    if (q == 'yes'):
                        open(path_w, mode="w").close()  # opens the fille to delete contents
                        # will write to the fille 
                        for i, word in enumerate(new_string.split()):
                            with open(path_w, mode="a") as write_file:
                                write_file.write(f"{i} : {word.title()},\n")
                                print(f"{i + 1} : {word.title()}")
                        return result
                    else:
                        print("--! not writing anything")
                        return
                else:
                    # this will just append the fille and append to it.
                    print("printing to fille")
                    for i, word in enumerate(new_string.split()):
                        # will write to the fille
                        with open(path_w, mode="a") as write_file:
                            write_file.write(f"{i} : {word.title()},\n")
                            print(f"{i + 1} : {word.title()}")
                    return result
        except:
            print("an error has accourd")
    """
    This function will take an fille.
    And write it out out as an Dictonary. And also write it out as fille.
    Defualt input filles: lorum.txt and random.txt
    Default output fille: new.txt
    """


def main() -> None:  # main function
    make_dict_and_write()


if __name__ == "__main__":  # intry point if the fille is ran
    main()
