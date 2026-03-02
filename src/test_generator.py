import random

def generate_test(k, m, max_id=20, filename= "tests/test.txt"):
    r = [random.randint(1, max_id) for _ in range(m)]
    with open(filename, "w") as f:
        f.write(f"{k} {m}\n")
        f.write(" ".join(map(str, r)) + "\n")


generate_test(k=10, m = 50, filename="tests/test1.txt")
generate_test(k=25, m=100,max_id=65, filename="tests/test2.txt")
generate_test(k=35, m=250, max_id= 100,filename="tests/test3.txt")