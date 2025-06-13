T = int(input())

"""
틀린 풀이 : 864가 나와야 하는데 826이 나옴

이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서
소설의 여러 장들이 '연속이 되도록' 파일을 합쳐나가고, 
최종적으로는 하나의 파일로 합친다.
"""

# for t in range(T):
#     K = input()
#     files = list(map(int, input().split()))
    
#     total = 0
    
#     while len(files) != 1:
#         files.sort()
        
#         # print(files)
        
#         min1 = files[0]
#         min2 = files[1]
#         files.remove(min1)
#         files.remove(min2)
        
#         temp = min1 + min2
#         files.append(temp)
        
#         total += min1 + min2
        
#         # print (f"{min1} + {min2} = {total}")
        
#     print(total)

for t in range(T):
    K = input()
    files = list(map(int, input().split()))
    
    total = 0
    
    while len(files) != 1:
        pass
    
    print(total)