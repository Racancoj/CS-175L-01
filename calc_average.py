# calc_average

def main():
    score1, score2, score3, score4, score5, average = calc_average()

    determine_grade(score1, score2, score3, score4, score5, average)

    repeat()

def calc_average():

    
    
    score1 = float(input('Enter score 1: '))
    score2 = float(input('Enter score 2: '))
    score3 = float(input('Enter score 3: '))
    score4 = float(input('Enter score 4: '))
    score5 = float(input('Enter score 5: '))
    
    total = score1 + score2 + score3 + score4 + score5

    average = total/NUM_SCORE
    

    return(score1, score2, score3, score4, score5, average)



def determine_grade(score1, score2, score3, score4, score5, average):

    print()

    letter_grade = ''

    print('Score   Numeric Grade  Letter Grade')
    print('-----------------------------------')
    
    if score1 >= 90 and score1 <= 100:
        letter_grade = 'A'
    elif score1 >= 80 and score1 <= 90:
        letter_grade = 'B'
    elif score1 >= 70 and score1 <= 79:
        letter_grade = 'C'
    elif score1 >= 60 and score1 <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    print(f'score 1:      {score1}      {letter_grade}')
        

    if score2 >= 90 and score2 <= 100:
        letter_grade = 'A'
    elif score2 >= 80 and score2 <= 90:
        letter_grade = 'B'
    elif score2 >= 70 and score2 <= 79:
        letter_grade = 'C'
    elif score2 >= 60 and score2 <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
        
    print(f'score 2:      {score2}      {letter_grade}') 

    if score3 >= 90 and score3 <= 100:
        letter_grade = 'A'
    elif score3 >= 80 and score3 <= 90:
        letter_grade = 'B'
    elif score3 >= 70 and score3 <= 79:
        letter_grade = 'C'
    elif score3 >= 60 and score3 <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    print(f'score 3:      {score3}      {letter_grade}')    

    if score4 >= 90 and score4 <= 100:
        letter_grade = 'A'
    elif score4 >= 80 and score4 <= 90:
        letter_grade = 'B'
    elif score4 >= 70 and score4 <= 79:
        letter_grade = 'C'
    elif score4 >= 60 and score4 <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    print(f'score 4:      {score4}      {letter_grade}')

    if score5 >= 90 and score5 <= 100:
        letter_grade = 'A'
    elif score5 >= 80 and score5 <= 90:
        letter_grade = 'B'
    elif score5 >= 70 and score5 <= 79:
        letter_grade = 'C'
    elif score5 >= 60 and score5 <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    print(f'score 5:      {score5}      {letter_grade}')

    if average >= 90 and average <= 100:
        letter_grade = 'A'
    elif average >= 80 and average <= 90:
        letter_grade = 'B'
    elif average >= 70 and average <= 79:
        letter_grade = 'C'
    elif average >= 60 and average <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    print(f'Average score: {average}   {letter_grade}')



def repeat():
    print()
    go_a_again = input('Do you want to repeat ')

    if go_a_again == 'yes':
        print()
        main()
    

           
NUM_SCORE = 5

main()
    
