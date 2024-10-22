def any(a):
    for i in a:
        if i==True:
            return True
            break
    else:
        return False

def all(a):
    for i in a:
        if i==False:
            return False
            break
    else:
        return True

def exactly(a,k):
    count=0
    for i in a:
        if i==True:
            count+=1

    if count==k:
        return True
    else:
        return False

def count(a):
    count=0
    for i in a:
        if i==True:
            count+=1
    return count


def _main():
    import stdio
    a = [False,False,True,False,True,True,True]
    stdio.writeln(any(a))
    stdio.writeln(all(a))
    stdio.writeln(exactly(a,3))
    stdio.writeln(count(a))

if __name__ == '__main__':
    _main()