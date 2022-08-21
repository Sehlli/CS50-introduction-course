def check ( text): # s is nember of senteces w nember of words  l nember of letters
    s=0
    l=0
    w=len(text.split(" "))
    for i in text :
        if i in [".","!","?"]:
            s=s+1    
    for j in text :
        if j  in list(map(chr, range(65, 123))):
            l=l+1  
# L is the average number of letters per 100 words in the text,and S is the average number of sentences per 100 words in the text
   
    L = l * 100 / w
    S = s * 100 / w
    index = round(0.0588 * L - 0.296 * S - 15.8)
    if (index < 1):
        print("Before Grade 1")

    elif (index >= 16):
        print("Grade 16+")
    else:
        print(f"Grade {index}")



text=input("Text : ") 
check(text)