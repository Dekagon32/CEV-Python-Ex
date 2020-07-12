def maior(*number):
    mai = number[0]
    print('Entre ',end='')
    for c in number:
        if c > mai:
            mai = c
        print(c,end=', ' if c != number[-1] else '. ')
    print('O maior é {}'.format(mai))



maior(1,7,4,7,2,5,12)
maior(0)