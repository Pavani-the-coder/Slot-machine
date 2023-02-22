import random #generate values in a machine randomly


MAX_LINES=3
MAX_BET=1000
MIN_BET=10

#SIZE OF A SLOT MACHINE
ROWS=3
COLS=3

#FREQUENCY OF EACH SYMBOL
symbol_count={
    "A":3,
    "B":8,
    "C":6,
    "D":4
}

#CHECK IF THE PERSON HAS ACTUALLY WON ANYTHING 
def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):# if lines=1 then line can take only 0 //ly if lines=2 then line=0 and 1
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check= column[line]
            if symbol!=symbol_to_check:
                break
        else:
                winnings+=values[symbol] * bet
                winning_lines.append(line+1)
    
    return winnings,winning_lines




#this generates a round of randomly chosen alphabets between A and D
def get_slotmachine_spin(rows,cols,symbols):
    all_symbol=[]
    for symbol,symbol_count in symbols.items(): #symbol is A and symbol count is 2 
        for _  in range(symbol_count):# _ is an anonymous symbol in the python
            all_symbol.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbol=all_symbol[:]#: is a slice operator and what ever changes we make in all doesnt effect current symbols.
        for _ in range(rows):
            value = random .choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#PRINT THE VALUES OF A SLOT MACHINE
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row], end=" | ")
            else:
                print (column[row], end="") #by default end is "\n" also known as new line character
        print()




#GETTING DEPOSIT
def deposit():
    while True:
        amount = input("Enter deposit amount: ")
        if amount.isdigit():#tells if digit is valid number or not
            amount=int(amount)
            if(amount > 0):#negitive numbers not allowed
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Enter a valid amount")
    return amount

#GETTING NUMBER OF LINES in other words getting the bet amount

def get_number_of_lines() :
    while True :
        lines=input("No of lines you want to bet between (1 - "+str(MAX_LINES)+"):") #added maxLine using concatenation by converting to string 
        if lines.isdigit():
            lines=int(lines)
            if(1<=lines<=MAX_LINES):
                break
            else:
                print("Enter lines between 1 and "+str(MAX_LINES))
        else :
            print("Enter a integer value")
    return lines

#PLACE BET AMOUNT

def place_bet():
    while True:
        bet=input("How much would you like to bet on each line? ")
        if bet.isdigit():
            bet=int(bet)
            if(MIN_BET<=bet<=MAX_BET):
                break
            else:
                print(f"Enter a bet amount between ${MAX_BET}-${MIN_BET}: ")
        else:
            print("Enter a number")
    return bet

def spin(balance):
    line=get_number_of_lines()
    while True:
        bet=place_bet()
        total=line *bet
        if total >balance :
            print(f"Your bet is greater than your balance")
        else:
            break

    print (f"You are betting ${bet} on {line} lines. The total bet is ${total} ")

    slots=get_slotmachine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winns,winlines=check_winnings(slots,line,bet,symbol_count)
    print(f"you have won ${winns}")
    print("you have won on lines",*winlines)
    return winns-total

def main():

    balance=deposit()
    #print (balance)
    while True:
        print(f"Your current balance is: ${balance}")
        ans=input("Press enter to continue or q to quit")
        if ans=='q':
            break
        balance+=spin(balance)
    print (f"your are left with ${balance}")

    

main()


