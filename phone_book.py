n = int(raw_input())
phone_book = {}
for _ in range(n):
    name, number = raw_input().split(" ")
    phone_book[name] = number

while True:
    try:
        query = raw_input()
        if query not in phone_book:
            print 'Not found'
        else:
            print '{}={}'.format(query, phone_book.get(query))
    except:
        break       

# while True and try/except accommodate the raw input of unknown amount