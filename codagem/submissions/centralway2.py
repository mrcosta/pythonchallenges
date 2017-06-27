#given x, menor y, que x * y  == um ou mais 4s seguidos de 0  or mais zeros
#4400, 440 ou 444 é valid

#vai ler o x e deduzir de  z = 2a + b, onde a é o numero de 4 e b de 0s
def get_input(counter):
    integers = []
    for count in range(0, counter):
        int_input = int(input())
        integers.append(int_input)
    return integers

def find_z_from_integers(integers):
    # 4, 40, 44, 400, 440
    # 1, 100, 110, 1000, 1100
    for integer in integers:
        if ((integer % 100) % 4):


def print_result(results):
    for result_z in results:
        print(result_z)

counter = int(input())
integers = get_input(counter)
results = find_z_from_integers(integers)
print_result(results)
