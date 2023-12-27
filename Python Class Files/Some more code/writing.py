with open('data.txt','w') as file:
    file.write('THis is the text written by python :)\n')
    file.write('THis is the second line text written by python :)')
    lines=['hello','this','is','a','line','maybe.. ?']
    file.writelines(lines)