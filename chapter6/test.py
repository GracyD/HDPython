def test(filename):
    try:
        data = open(filename).readline()
        print("Yes, it is there.")
        return(data)
    except:
        print("There is no such file.")
        return(None)
    finally:
        print("Anyway, the finally is running.")


print(test('sarah2.txt'))

print(test('sarah1.txt'))






