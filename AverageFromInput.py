# AverageFromInput
# CS-175
# spring 2022
# Therese Racancoj

def main():
    total = 0
    count = 0
 
    number_file = open('numbers.txt', 'r')

 
    for line in number_file:

        num = float(line)

        count += 1

        total += num 

        print(f'I read in {count} number(s) Current number is:\
 {num:.2f}  Total is: {total:.2f}')

    average = total/count
    
    print(f'Average: {average}')
    
    number_file.close()


if __name__ == '__main__':
    main()



