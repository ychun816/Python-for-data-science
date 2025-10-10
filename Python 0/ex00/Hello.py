#subject
ft_list  = ["Hello", "tata!"]     # -> ['Hello', 'World!']   
ft_tuple = ("Hello", "toto!")     # -> ('Hello', 'France!')
ft_set   = {"Hello", "tutu!"}     # -> {'Hello', 'Paris!'}
ft_dict  = {"Hello" : "titi!"}    # -> {'Hello': '42Paris!'}

#your code here
ft_list[1] = "World!" #changable
ft_tuple = (ft_tuple[0], "France!") #not changeable -> create another new one
ft_set = {"Hello", "Paris!"} #no fixed oder -> have to recreate
ft_dict["Hello"] = "42Paris!" # Change value for key "Hello"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

### expected output ###
# $>python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>

### NOTES ###
# list : like array in c, can change value by index
# tuple : fixed order / fixed value, cannot change value -> have to recreate
# set : no fixed order / remove dups
# dict :  [index] : [value] Stores data in key → value pairs (like container in c++)

