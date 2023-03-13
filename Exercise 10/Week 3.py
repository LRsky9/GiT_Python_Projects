#print('\tthis isn\'t \n\t\t very easy \u00A1')

#print("L\u0024ure\u0376")

#text = 'Finished files are the result of years of scientific study combined with the experience of years'
#print(text.count ('f'), ('F'))

#letter_count = {}

#for letter in text:
  #  if letter.isalpha():
 #       letter_count[letter.lower()] = letter_count.get(letter.lower(), 0) + 1

#print(letter_count)



#name = 'james'
#second_name = 'Bond'

#print('the name is {1}, {0} {1}'.format(name, second_name))

#‘ThisIsAReallyLongStringThatIsFunToConvert’
#'1. PascalCase to snake_case
#''‘this_is_a_really_long_string_that_is_fun_to_convert’
#'2. snake_case to PascalCase
#3. Is one an anagram of the other?
#* “wholesome python activity”
#* “Woven Polytheistic Mat Toy”


#pascal = 'ThisIsAReallyLongStringThatIsFunToConvert'

#print(str.split(pascal))

#print('_'.join(pascal))

#snake = 'this_is_a_really_long_string_that_is_fun_to_convert'

#print(''.join(snake))


#Task 1
pascal = "ThisIsAReallyLongStringThatIsFunToConvert"
snake_case_s = ''.join(['_'+i.lower() if i.isupper() else i for i in pascal]).lstrip('_')
print(snake_case_s)


#Task 2
import string
snake = "this_is_a_really_long_string_that_is_fun_to_convert"
res = string.capwords(snake.replace("_"," ")).replace(" ", "")
print(str(res))