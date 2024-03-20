#!/usr/bin/python3

# a UTF-8 encoded fille
# path = "./lorum.txt"


    # In [13]: with open("./lorum.txt", mode="r") as fille:
    # ...:     y = set()
    # ...:     for y in fille:
    # ...:         print(y)
    # ...:     print(f'we have a list of {set(y) for y in fille}')

# ToDo
# const vars for filles, check out random.txt ":" bug at the end of the fille

from json import dump

PATH_LORUM = "./files/input/lorum.txt"
PATH_RANDOM = "./files/input/random.txt"
PATH_NEW_FILLE="./files/output/new.txt"


def write_to_fille(Path, Input):
    New_string = Input.ltranslate({ord(','):None}).translate({ord('.'):None})
    Result = { 0 : ""}
    for i, word in enumerate(New_string.split()):
        with open(Path, mode="a") as write_file:
            write_file.write(f"{i} : {word.title()},\n")
            print(f"{i + 1} : {word.title()}")
    """
    This will write the given input to a given fille.
    """
    return Result


def write_input_to_json(path, input):
    str_input = input 
    print("-- :", str_input, "\n and type of:", type(str_input))
    with open(path, mode="w") as fille:
        dump(input, fille)
   
def make_dict(path=PATH_LORUM): 
    with open(path, mode="r") as fille: 
        string = fille.read()
        n_string = string.translate({ord(','):None}).translate({ord('.'):None})
        result = {} 
        for i, word in enumerate(n_string.split()):
            result[i] = word.title() 
            print(f"{i + 1} : {word.title()}") 
        # print(result)

    """
    This function will take an fille.
    And write it out out as an Dictonary.
    """
    return result


def make_dict_and_write(path=PATH_LORUM, path_w=PATH_NEW_FILLE):
    with open(path, mode="r") as file:
        string = file.read()  # puts the fille into a string type 
        # cleans it up 
        n_string = string.translate({ord(','):None}).translate({ord('.'):None})
        # result = {0 : ""} # creates a dictonary 
        print(n_string)
        try:
            with open(path_w, mode="r") as test_read:
                if (len(test_read.read()) > 2):  # testing if the fille is empty
                    q = input("-- The fille isn't empy do you wish to overwerite? yes or no: ")
                    if (q == 'yes'):
                        open(path_w, mode="w").close()  # opens the fille to delete contents
                        return write_to_fille(path_w, string) 
                    else:
                        print("--! not writing anything")
                        return
                else:
                    # this will just append the fille and append to it.
                    print("printing to fille")
                    # will write to the fille
                    return write_to_fille(path_w, string)
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
    test_dict = make_dict()
    print("-- :", test_dict, "\n and type of:", type(test_dict))
    write_input_to_json("./files/output/test.json", test_dict)

if __name__ == "__main__":  # intry point if the fille is ran
    main()
