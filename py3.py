def say_hello(name):
  # you can print to STDOUT to debug if you need to:
    if name:
        greeting = 'Hello, ' + name + '!'
    else:
        greeting = "Hello there!"

    return greeting


def dashitize(num):
    """take in num, return it with dashes before and after odd digits in num"""

    new_num = str(num)
    dashed = new_num[0]
    for i in range(1, len(new_num)):
        if int(new_num[i]) % 2 == 0:
            dashed += new_num[i]
        elif int(new_num[i]) % 2 != 0 and dashed[-1] != '-':
            dashed += '-' + new_num[i] + '-'
        elif dashed[-1] == '-':
            dashed += new_num[i] + '-'
    if dashed[-1] == '-':
        dashed = dashed[:-1]
    return dashed
