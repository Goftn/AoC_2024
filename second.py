import sys

def main(filename):
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
            
    left_list.sort()
    right_list.sort()
        
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])

    print(total_distance)
    
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_list.count(number)
        
    print(similarity_score)
    
if __name__ == '__main__':
    main(sys.argv[1])