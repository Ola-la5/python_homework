#task 1
def hello():
    return "Hello!"
print (hello())

#task 2 
def greet(name):
    return "Hello, "+name+"!"
print (greet("Name"))

#task 3 
def calc(a,b,do = "multiply"):
    try:

       
        if do=="multiply":
            result=a*b
        elif do =="add":
            result=a+b
        elif do =="subtract":
            result=a-b
        elif do =="divide":
         result=a/b
        elif do=="modulo":
            result=a%b
        elif do =="int_divide":
            result=a//b
        elif do=="power":
            result=a**b
    
        return result
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
 

print(calc(5,2,"multiply"))
print(calc(5,2,"add"))   
print(calc(5,2,"subtract"))
print(calc(5,7,"subtract"))
print(calc(5,2,"divide"))
print(calc(5,2,"modulo"))
print(calc(5,2,"int_divide"))
print(calc(5,2,"power"))
print(calc(5,0,"divide"))
print(calc("2","2","multiply"))

#task 4 
def data_type_conversion (value,type =""):
    try:
        if type=="float":
            out=float(value)
        elif type=="str":
            out=str(value)
        elif type =="int":
            out = int(value)
        return out

    except ValueError:
        return f"You can't convert {value} into a {type}."
    
print(type(data_type_conversion(5,"float")))
print(type(data_type_conversion(5,"str")))
print(type(data_type_conversion(5,"int")))
print(data_type_conversion("noncence","float"))

#task 5 
def grade(*args):
    try:

        average = sum(args)/len(args)
        if average >=90:
            out = "A"
        elif average <=89 and average >= 80:
            out = "B"
        elif average <=79 and average >=70:
            out = "C"
        elif average <=69 and average >=60:
            out = "D"
        else:
            out ="F"

        return out
    except TypeError:
        return "Invalid data was provided."
print (grade(90,99,95,92))
print (grade(80,89,85,82))
print (grade(70,79,75,72))
print (grade(60,69,65,62))
print (grade(50,59,55,52))
print (grade("a","c","hi","blob"))

#task 6
def repeat(string = "", count=0):
    out = ""    
    for num in range(count):
        out+=string
    return out        
print (repeat("blob ",5))

#task 7 
def student_scores(position = "", **kwargs):
    
    if position =="best":
            return max(kwargs, key = kwargs.get)
    elif position =="mean":
            return sum(kwargs.values())/len(kwargs)

print(student_scores("best", Piglet = 90, Io = 55, Winnie = 100))
print(student_scores("mean", Piglet = 90, Io = 55, Winnie = 100))

#task 8
def titleize(name=""):
    words = name.split()
    out = ""
    for i, word in enumerate(words):
        if i ==0 or i ==len(words)-1:
            words[i] = word.capitalize()
        
        elif word =="a" or word =="on" or word =="an" or word == "the" or word=="of" or word=="and" or word=="is" or word=="in":   
            words[i] = word
        else:
            words[i] = word.capitalize()

    out = " ".join(words)
    
    return out

print (titleize("the best book"))
print (titleize("Alise in wonderland"))

#task 9
def hangman(secret ="", guess =""):
    out = ""
    for char in secret:
        if char in guess:
            out+=char
        else:
            out +="_"    
    return out

print (hangman("blob","bo"))

#task 10
def pig_latin (input=""):
    words = input.split()
    out = ""
    for word in words:
        #starts with vowel
        if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
            out+=word+"ay"+" "
        #starts with qu
        elif word[0]=="q" and word[1] =="u":
            temp=""
            count=2
            while count<len(word):
                temp+=word[count]
                count+=1    
            out+=temp+"quay"+" "
        #starts with one or few consonant
        else:
            temp = ""
            count = 0
            #find the first vowel
            while count <len(word) and word[count] not in ("a", "e", "i", "o", "u"):
                #handle "qu" in the middle of the word after consonant
                if count+1 < len(word) and word[count] == 'q' and word[count+1] == 'u':
                    count += 2
                else:
                    count += 1
            #new word after first vowel
            i=count
            while i <len(word):
                temp+=word[i]
                i+=1
            #add part before first vowel
            i=0
            while i<count:
                temp+=word[i] 
                i+=1
            #add ay
            out+= temp+"ay"+" "   

    return out.strip()
print(pig_latin("apple"))
print(pig_latin("sweet apple"))
print(pig_latin("greek apple"))
print(pig_latin("queen"))