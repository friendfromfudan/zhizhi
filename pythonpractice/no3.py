def even_or_odd(num):
    return 'even' if num%2==0 else 'odd'

# print(even_or_odd(4))

def get_issure(num_str):
    n=len(num_str)
    if n==15 and num_str[0:2] in ['34','27']:
        return 'AMEX'
    elif n==16 and num_str[0:4] in '6011':
        return 'Discover'
    else:
        return 'Unkonwn'


print(get_issure('341111111111111'))