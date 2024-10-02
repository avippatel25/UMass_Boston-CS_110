import stdio
import stdrandom

# random club is selected for a card
club=stdrandom.uniformInt(1,5)

# random card is selected from one of the club
card_num=stdrandom.uniformInt(1,14)

# the name and number is assigned to card
if club==1:
    if card_num==13:
        stdio.writeln("King of Hearts")
    elif card_num==12:
        stdio.writeln("Queen of Hearts")
    elif card_num==11:
        stdio.writeln("Jack of Hearts")
    elif card_num==10:
        stdio.writeln("10 of Hearts")
    elif card_num==9:
        stdio.writeln("9 of Hearts")
    elif card_num==8:
        stdio.writeln("8 of Hearts")
    elif card_num==7:
        stdio.writeln("7 of Hearts")
    elif card_num==6:
        stdio.writeln("6 of Hearts")
    elif card_num==5:
        stdio.writeln("5 of Hearts")
    elif card_num==4:
        stdio.writeln("4 of Hearts")
    elif card_num==3:
        stdio.writeln("3 of Hearts")
    elif card_num==2:
        stdio.writeln("2 of Hearts")
    elif card_num==1:
        stdio.writeln("Ace of Hearts")
elif club==2:
    if card_num==13:
        stdio.writeln("King of Spades")
    elif card_num==12:
        stdio.writeln("Queen of Spades")
    elif card_num==11:
        stdio.writeln("Jack of Spades")
    elif card_num==10:
        stdio.writeln("10 of Spades")
    elif card_num==9:
        stdio.writeln("9 of Spades")
    elif card_num==8:
        stdio.writeln("8 of Spades")
    elif card_num==7:
        stdio.writeln("7 of Spades")
    elif card_num==6:
        stdio.writeln("6 of Spades")
    elif card_num==5:
        stdio.writeln("5 of Spades")
    elif card_num==4:
        stdio.writeln("4 of Spades")
    elif card_num==3:
        stdio.writeln("3 of Spades")
    elif card_num==2:
        stdio.writeln("2 of Spades")
    elif card_num==1:
        stdio.writeln("Ace of Spades")
elif club==3:
    if card_num==13:
        stdio.writeln("King of Clubs")
    elif card_num==12:
        stdio.writeln("Queen of Clubs")
    elif card_num==11:
        stdio.writeln("Jack of Clubs")
    elif card_num==10:
        stdio.writeln("10 of Clubs")
    elif card_num==9:
        stdio.writeln("9 of Clubs")
    elif card_num==8:
        stdio.writeln("8 of Clubs")
    elif card_num==7:
        stdio.writeln("7 of Clubs")
    elif card_num==6:
        stdio.writeln("6 of Clubs")
    elif card_num==5:
        stdio.writeln("5 of Clubs")
    elif card_num==4:
        stdio.writeln("4 of Clubs")
    elif card_num==3:
        stdio.writeln("3 of Clubs")
    elif card_num==2:
        stdio.writeln("2 of Clubs")
    elif card_num==1:
        stdio.writeln("Ace of Clubs")
else :
    if card_num==13:
        stdio.writeln("King of Diamonds")
    elif card_num==12:
        stdio.writeln("Queen of Diamonds")
    elif card_num==11:
        stdio.writeln("Jack of Diamonds")
    elif card_num==10:
        stdio.writeln("10 of Diamonds")
    elif card_num==9:
        stdio.writeln("9 of Diamonds")
    elif card_num==8:
        stdio.writeln("8 of Diamonds")
    elif card_num==7:
        stdio.writeln("7 of Diamonds")
    elif card_num==6:
        stdio.writeln("6 of Diamonds")
    elif card_num==5:
        stdio.writeln("5 of Diamonds")
    elif card_num==4:
        stdio.writeln("4 of Diamonds")
    elif card_num==3:
        stdio.writeln("3 of Diamonds")
    elif card_num==2:
        stdio.writeln("2 of Diamonds")
    elif card_num==1:
        stdio.writeln("Ace of Diamonds")