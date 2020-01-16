# Eric Broadbent
# 12/19
# Word Search
print()
print()
#imports
import random
#adding this in git

# constance
# game data
PUZZLE = "KPVGQFLOATGUJQMTXAQIWDEMXNDMYZAWRISEACGEIUUHKHXIELIKIVXRNJIERRAPAQAGYSTHEQPSCBYNEJOSKSLWXWRPLZOAHLIKUOVRZOIEEITENOITCNUFTNMQTSVLODVVBOEATSTIIZZOSPMNLIREZXDLDDPORSAMIEGHENIPZHSBKVCMPEFDOCGQVPYPUWPORRNCRFJBKMVNEODOWIMTAJPFRYDPE"
DPUZZLE = "KPVGQFLOATGUJQMTXAQIWDEMXNDMYZAWRISEACGEIUUHKHXIELIKIVXRNJIERRAPAQAGYSTHEQPSCBYNEJOSKSLWXWRPLZOAHLIKUOVRZOIEEITENOITCNUFTNMQTSVLODVVBOEATSTIIZZOSPMNLIREZXDLDDPORSAMIEGHENIPZHSBKVCMPEFDOCGQVPYPUWPORRNCRFJBKMVNEODOWIMTAJPFRYDPE"


col0 = ["K","T","A","H","R","S","R","O","T","A","R","E","P","O","D",]
col1 = ["P","X","W","X","R","C","P","I","N","T","E","G","E","R","O",]
col2 = ["V","A","R","I","A","B","L","E","M","S","Z","H","F","R","W",]
col3 = ["G","Q","I","E","P","Y","Z","E","Q","T","X","E","D","N","I",]
col4 = ["Q","I","S","L","A","N","O","I","T","I","D","N","O","C","M",]
col5 = ["F","W","E","I","Q","E","A","T","S","I","L","I","C","R","T",]
col6 = ["L","D","A","K","A","J","H","E","V","Z","D","P","G","F","A",]
col7 = ["O","E","C","I","G","O","L","N","L","Z","D","Z","Q","J","J",]
col8 = ["A","M","G","V","Y","S","I","O","O","O","P","H","V","B","P",]
col9 = ["T","X","E","X","S","K","K","I","D","S","O","S","P","K","F",]
col10 = ["G","N","I","R","T","K","U","T","V","P","R","B","Y","M","R",]
col11 = ["U","D","U","N","H","L","O","C","V","M","S","K","P","V","Y",]
col12 = ["J","M","U","J","E","W","V","N","B","N","A","V","U","N","D",]
col13 = ["Q","Y","H","I","Q","X","R","U","O","L","M","C","W","E","P",]
col14 = ["M","Z","K","E","P","W","Z","F","E","I","I","M","P","O","E",]
puzzle2d = [col0,col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14]


WORDS =["STRING",#(85,70,55,40,25,10)
        "INTEGER",#(106,121,136,151,166,181,196)
        "FLOAT",#(5,6,7,8,9)
        "BOOLEAN",#(175,159,143,127,111,95,79)
        "LIST",#(155,140,125,110
        "VARIABLE",#(2,17,32,47,62,77,92,107)
        "INDEX",#(213,198,183,168,153)
        "FUNCTION",#(119,118,117,116,115,114,113,112)
        "LOGIC",#(97,82,67,52,37)
        "OPERATORS",#(195,180,165,150,135,120,105,90,75)
        "CONDITIONALS"#(199,184,169,154,139,124,109,94,79,64,49,34)
        ]

QUESTIONS = ["what data type do you wrap in \" \" when you assign it to a variable",
             "What data type can only hold whole numbers",
             "What data type can hold fractunal numbers",
             "What data type holds True or False values",
             "name a data structure that can be changed (Mutable)",
             "What do you call a container to store values",
             "the number that can select a position of a single element in a list is the ___ position",
             "A block of code that preforms a single action and preforms it well and can be called up using a single phrase is a what?",
             "boolean _____ allows our program to make disicions that can be reduced to a true false answer",
             "_________ allow us to preform math matical operations like + - * / < > ",
             "in an if statment a ____________ must evaluate to true befor the if block can be ran."]


# game data
picked = []

# functions
def random_question(words,questions,picked):
    """gets a random Question"""
    while WORDS:
        choice = random.randrange(0,len(WORDS))
        if choice not in picked:
            question = questions[choice]
            answer = words[choice]
            picked.append(choice)
            return question, answer
        

def get_word_position(puzzle):
    while True:
        letters = []
        nums = []
        number = ""
        pos = input("Enter the index positions for the word you are looking for\nbe sure to sererate each position with a ,\n")
        for i in pos:
            if i != ",":
                number = number + i
            else:
                if number.isdigit():
                    letters.append(puzzle[int(number)])
                    nums.append(int(number))
                    number = ""
                else:
                    print("must enter numbers")
                    continue
        if number.isdigit():
            letters.append(puzzle[int(number)])
            nums.append(int(number))
        else:
            print("must enter numbers")
            continue
        # if up down left right or diaginal 
        if nums[0] -1 == nums[1] or nums[0] +1 == nums[1] or nums[0] +15 == nums[1] or nums[0] -15 == nums[1] or nums[0] +16 == nums[1] or nums[0] -16 == nums[1] or nums[0] +14 == nums[1] or nums[0] -14 == nums[1]:
        
            word = ""
        
            for i in letters:
                word = word+i
            return word
        else:
            print("must use consecutive positions vertically horizontally or diagonally")
        





def display_puzzle(puzzle,colums,rows):
    """displays Puzzel"""
    i = 0
    print("     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14")
    
    for col in range(colums):
        if col < 10:
            line = str(col)+"  | "
        else:
            line = str(col)+" | "
         
        for row in range(rows):
            line += puzzle[i]+" | "
            i += 1
        print(line)
        
def display_puzzle2(puzzle):
    print(puzzle[0:14])
    print(puzzle[15:29])
    print(puzzlel[30:44])
    print(puzzle[45:59])
    print(puzzle[60:74])
    print(puzzle[75:89])
    print(puzzle[90:104])
    print(puzzle[105:119])
    print(puzzle[120:134])
    print(puzzle[135:149])
    print(puzzle[150:164])
    print(puzzle[165:179])
    print(puzzle[180:194])
    print(puzzle[195:209])
    print(puzzle[210:224])




def display_puzzle3():
    grid = str.format("""
   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
  ----------------------------------------------
0 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
1 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
2 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
3 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
4 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
5 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
6 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
7 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
8 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
9 |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
10|{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
11|{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
12|{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
13|{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
14|{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |{} |
  ----------------------------------------------
""","K","P","V","G","Q","F","L","O","A","T","G","U","J","Q","M","T","X","A","Q","I","W",
"D","E","M","X","N","D","M","Y","Z","A","W","R","I","S","E","A","C","G","E","I","U","U",
"H","K","H","X","I","E","L","I","K","I","V","X","R","N","J","I","E","R","R","A","P","A",
"Q","A","G","Y","S","T","H","E","Q","P","S","C","B","Y","N","E","J","O","S","K","S","L",
"W","X","W","R","P","L","Z","O","A","H","L","I","K","U","O","V","R","Z","O","I","E","E",
"I","T","E","N","O","I","T","C","N","U","F","T","N","M","Q","T","S","V","L","O","D","V",
"V","B","O","E","A","T","S","T","I","I","Z","Z","O","S","P","M","N","L","I","R","E","Z",
"X","D","L","D","D","P","O","R","S","A","M","I","E","G","H","E","N","I","P","Z","H","S",
"B","K","V","C","M","P","E","F","D","O","C","G","Q","V","P","Y","P","U","W","P","O","R",
"R","N","C","R","F","J","B","K","M","V","N","E","O","D","O","W","I","M","T","A","J","P",
"F","R","Y","D","P","E")
    print(grid)
    


def get_word_2d(puzzle):
    letters = []
    nums = []
    number = ""
    pos = input("Enter the index positions for the word you are looking for\nbe sure to sererate each position with a ,\n")
    for i in pos:
        if i != ",":
            number = number + i
        else:
            if number.isdigit():
                nums.append(int(number))
                number = ""
    nums.append(int(number))
    word = ""
    while nums:
        x = nums.pop(0)
        y = nums.pop(0)
        word = word + puzzle[y][x]
        
    return word

def game():
    

    
    count = 0
    gameOver = len(WORDS)
    while count != gameOver:
        display_puzzle(DPUZZLE,15,15)
        print()
        q,a = random_question(WORDS,QUESTIONS,picked)
        print(1,q)
        print()
        correct = False
        while correct == False:
            word = get_word_position(PUZZLE)
            print(word)
            if word == a:
                correct = True
                count += 1
                print("you got it")
    print("thats it you got them all")
    print("thanks for playing")
        



game()


