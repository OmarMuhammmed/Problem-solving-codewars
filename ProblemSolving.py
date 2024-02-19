# 1.Reversed Words ==> codewares 
def reverse_words(s):
    
    My_list = s.split(' ') # to transfer from string to list 

    My_reversed_list = My_list[::-1] # To reflect the list 

    My_reversed_text = " ".join(My_reversed_list) # To trensfer From list to string with sep 
    
    return My_reversed_text
    
    # abbreviated solution 
    
    return " ".join(s.split(' ')[::-1])

# 2.Keep HydratedKeep! ==> codewares 
def litres(time):
    
    return time //2 
    
    # anthor solution 
    
    return int(time*0.5)

# 3.Filter out the Geese ==> codewares
def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    my_words=[]
    for item in birds :
        if item not in geese :
            my_words.append(item)
    return my_words        
    
    # abbreviated solution
    return [bird for bird in birds if bird not in geese] 

# 4.Beginner Series #2 Clock ==> codewares 
def past(h, m, s):

    return h*60*60*1000+ m * 60*1000 + s*1000

# 5.Invert Values ==> codewares
def invert(lst):
    new_list= [ ]
    for num in lst :
        if num > 0 : # +
            num = - num
            new_list.append(num)
        elif num < 0 : # - 
            num = - num 
            new_list.append(num)
    return new_list
    
    # anthor solution 
            
    return [-x for x in lst]

# 6.Pirates!! Are the Cannons ready!?? ==> codewares 
def cannons_ready(gunners):
    for gun in gunners.values() :
        if gun == "ney" :
            return "Shiver me timbers!"
    
    return "Fire!"
    
    # anthor solution 
    
    return 'Shiver me timbers!' if 'nay' in gunners.values() else 'Fire!'

# 7.Miles per gallon to kilometers per liter ==> codewares 
def converter(mpg):
    kpl = mpg * 1.609344 / 4.54609188 
    return round(kpl,2)    
      
# 8.Finish Guess the Number Game ==> codewares 
def __init__(self, number, lives):
    self.number = number
    self.lives = lives

def guess(self,n):
    if self.lives == 0:
        raise  ('Omae wa mo shindeiru')
    elif n  == self.number:
        return True
    self.lives -= 1
    return False

# 9.Count the Monkeys! ==> codewares
def monkey_count(n):
    My_list = [ ]
    for num in range(1,n+1) :
        My_list.append(num)
    return  My_list  
    # anthor Solution
    return list(range(1,n+1)) 

# 10.Gravity Flip ==> codewares
def flip(d, a):
    if d == "R":
      solution = sorted(a) 
    elif d == "L" :
      solution = sorted(a, reverse=True)    
    else :
        return None 
    return solution

# 11.carsh override ==> codewares 
def alias_gen(f_name, l_name):
    # if f_name[0].upper() not in FIRST_NAME or l_name[0].upper() not in SURNAME:
        return 'Your name must start with a letter from A - Z.'
    # else :
        # return FIRST_NAME[f_name[0].upper()]+ " "+ SURNAME[l_name[0].upper()]

# 12.Price of Mangoes ==> codewars
def mango(quantity, price):
    l=[]
    for i in range(1,quantity+1):
        if i % 3 != 0 :
            l.append(i) 
    return len(l)*price
    # anthor solution
    return (quantity - quantity // 3) * price

# 13.Calculate BMI ==> codewares 
def bmi(weight, height):
    BMI = weight/height**2
    if BMI <= 18.5 :
         return "Underweight"
    elif BMI <= 25.0 :
        return "Normal"
    elif BMI <= 30.0 :
        return "Overweight" 
    elif BMI > 30 :
        return "Obese"
    
# 14.Vowel remover ==> codewares
def shortcut( s ):
    sol=[]
    for L in s :
        if L not in ["a", "e", "i", "o", "u"] :
            sol.append(L)
        elif L.isupper():
            return s
    return "".join(sol)
    # anthor solution
    return ''.join(c for c in s if c not in 'aeiou')    

# 15. Convert a String to a Number! ==> codewares 
def string_to_number(s):
    return int(s)
              
# 16.Coloured Triangles ==> codewares(MidLevel)
def triangle(row):
    while len(row) > 1:
        new_row = ''
        for i in range(len(row) - 1):
            pair = row[i:i+2]
            if pair == "RR" or pair == "GG" or pair == "BB":
                new_row += pair[0]
            elif "R" in pair and "G" in pair:
                new_row += "B"
            elif "R" in pair and "B" in pair:
                new_row += "G"
            elif "G" in pair and "B" in pair:
                new_row += "R"
        row = new_row
    return row
      
# 17.Remove First and Last Character ==> codewares
def remove_char(s):
    return s[1:-1]

# 18.Sum of array singles ==> codewares 
def repeats(arr):
    return sum([x for x in arr if arr.count(x) == 1])
# 19.Shortest Word ==>codewares 
def find_short(s):
    short = s.split()
    short1 = min(short,key=len)
    l = len(short1)   
    return l # l: shortest word length
    
# 20.Beginner Series #3 Sum of Numbers ==> codewares
def get_sum(a,b):
  sol = []
  if a >= b :  
    for I in range(b, a+1) :
      sol.append(I)

  elif a <= b :
    for I in range(a, b+1) :
      sol.append(I)

  elif a == b :
      sol.append(a)    
  
  return  sum(sol)  

# 21.Jaden Casing Strings ==> codewares
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
def to_jaden_case(string):
  words = string.split()
  cap_words = [word.capitalize() for word in words] 
  return " ".join(cap_words) 
  # anthor solution 
  return ' '.join(word.capitalize() for word in string.split())
