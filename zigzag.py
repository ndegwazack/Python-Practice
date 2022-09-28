import time, sys

indent = 0 #No. of space to indent
indentIncreasing = True #whether indentation is increasing or not

try:
    while True: #main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #pause for 0.1s

        if indentIncreasing:
            #increase no of spaces
            indent += 1
            if indent == 20:
                #change direction
                indentIncreasing = False

        else:
            #decrease no of spaces
            indent -= 1
            if indent == 0:
                #change direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()