def  consecutive(num):
    count = 0
    times = 0
    for current in range(1, num + 1):
        sum = current
        next = current + 1
        while (sum < num):
            sum+= next
            if (sum == num):
                count+= 1
            next+=1
            times+=1
    print(times)
    return count

def triangleOrNot(first_flower, second_flower, third_flower):
    sum_first_flower = sum(first_flower)
    sum_second_flower = sum(second_flower)
    sum_third_flower = sum(third_flower)
    is_valid_triangule = "Yes" if is_triangule(sum_first_flower, sum_second_flower,
                                         sum_third_flower) else "No"

    return is_valid_triangule

def is_triangule(sum_first_flower, sum_second_flower, sum_third_flower):
    return ((sum_first_flower + sum_second_flower > sum_third_flower) and
(sum_first_flower + sum_third_flower > sum_second_flower) and
(sum_second_flower + sum_third_flower >
                                                  sum_first_flower))

#print(triangleOrNot([1, 1, 1], [2, 1, 1], [1, 1, 1, 2]))
print(consecutive(15))

def  bestTrio(friends_nodes, friends_from, friends_to):
    graph = {}
    count = 0

    for i in range(0, friends_nodes):
        if friends_from[i] in graph:
           graph[friends_from[i]].append(friends_to[i])
        else:
            graph[friends_from[i]] = [friends_to[i]]

    #for key, value in graph.items():
    #    if value[1] in graph[value[0]]
    #        count+ = 1

    return count


#print(bestTrio(5, [1, 1, 2, 2, 3, 4], [2, 3, 3, 4, 4, 5]))
