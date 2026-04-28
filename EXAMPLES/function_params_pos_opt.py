def search_files(search_term, *file_paths):
    for file_path in file_paths: # file_paths is tuple of arguments
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    print(raw_line.rstrip()) # remove \n

search_files("bird", "../DATA/alice.txt", "../DATA/parrot.txt")

#  def foo(*args): 
# foo()
# foo(1)
# foo(1, 2, 3)

def wombat(**kwargs):
    for name, value in kwargs.items():
        print(name, value)

wombat(color='blue', city="Durham", person='Amit')
# wombat('blue', 'Durham')

def toast(*args, **kwargs):
    pass
# toast()
# toast(1, 2, 3)
# toast(name="Fred")
# toast(1, 2, name="Fred", city="Des Moines")

def locate(*, city, state):
    pass

# locate(city="Pittsburgh", state="PA")
# locate(state="VA", city="Norfolk")



    
