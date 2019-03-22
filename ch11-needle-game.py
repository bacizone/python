for i in range(0, 1000):
    filename = 'c:\sourceCode\headfirstlearntocode-master\ch9\needle\' + str(i) + '.txt'
    file = open (filename, 'r')
    text = file.read()
    if 'needle' in text:
        print('Found needle in file ' + str(i) + '.txt')
    file.close ()