#Using eval()

if __name__ == '__main__':
    N = int(input())
    lista = []
    for _ in range(N):
        params = input().split()
        cmd = params.pop(0) 
        if cmd == 'print':
            print(str(lista))            
        else:    
            eval('lista.' + cmd + '(' + ','.join(params) + ')')