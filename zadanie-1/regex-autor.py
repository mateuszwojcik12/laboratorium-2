import re as re

def function_check_regex():
    autor1 = 'Agnieszka'
    autor2 = 'Mateusz'
    print(re.search(r"Ag[aęąio]|Adze|Agnieszk[aoięą]|Agnieszc[e]", autor1))
    print(re.search(r"Mateus.", autor2))

if __name__ == '__main__':
    function_check_regex()


