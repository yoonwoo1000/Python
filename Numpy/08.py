import numpy as np

# numpy에서 제공하는 메소드들
# 0~100 사이의 정수를 시험 점수 : 10개 이상
np_array = np.array([99, 80, 87, 65, 70, 75, 84, 73, 91, 30, 62])

# 1차원 배열 / 2차원 배열
# 원소의 총합
print(np.sum(np_array))
"""
# 원소 개수
print(np_array.size)
sum = 0
for i in range(np_array.size) :
    sum += np_array[i]
print(sum)
"""
# 평균값
print(np.mean(np_array))
"""
sum = 0
for i in range(np_array.size) :
    sum += np_array[i]
print(sum/np_array.size)
"""
# 최소값
print(np.min(np_array))
"""
min_value = 100
for i in range(np_array.size) :
    if min_value >= np_array[i] :
        min_value = np_array[i]
print(min_value)
"""
# 최대값
print(np.max(np_array))
"""
max_value = 0
for i in range(np_array.size) :
    if max_value <= np_array[i] :
        max_value = np_array[i]
print(max_value)
"""
# 표준편차
"""표준 편차(標準 偏差, 영어: standard deviation, SD)는 통계집단의 분산의 정도 또는 자료의 산포도를 나타내는 수치로, 분산의 음이 아닌 제곱근 즉, 분산을 제곱근한 것으로 정의된다"""
print(np.std(np_array))
# 중간값 : 배열의 중간에 위치한 값 / 최빈값 -> X
# 오름차순 정렬
np_array.sort()
print(np_array)
# 슬라이싱을 통해 순서 역전
np_result = np_array[::-1]
print(np_result)
# 중간값
print(np.median(np_array))

np_array = np.array([1, 1, 1, 1, 5, 10, 10, 15, 20, 20])
# 데이터 개수 10개
# 데이터 종류 : 5종 1,5,10,15,20
# 데이터 고유값만 가져오기
result = np.unique(np_array)
print(result)
# 데이터 고유값 과 각 고유값의 빈도
(values, counts) = np.unique(np_array, return_counts=True)
print(values)
print(counts)

# 2차원 배열은 방향성을 지정
np_array = np.array([[91, 82, 73, 64, 55], [66, 77, 88, 99, 100], [11, 12, 13, 14, 15]])
print(np_array)
# np.메소드(배열,방향)
"""
[[ 91  82  73  64  55]      -> 행의 총합 -> 365 / 평균 73
 [ 66  77  88  99 100]      -> 행의 총합 -> 430 / 평균 86
 [ 11  12  13  14  15]]     -> 행의 총합 -> 65  / 평균 13
    |
열총합
   168
평균56
"""
print("열방향 합계 : ", np.sum(np_array, axis=0))
print("행방향 합계 : ", np.sum(np_array, axis=1))
# min, max, mean, std, median
print("열방향 최소값 : ", np.min(np_array, axis=0))
print("행방향 최소값 : ", np.min(np_array, axis=1))
print("열방향 최대값 : ", np.max(np_array, axis=0))
print("행방향 최대값 : ", np.max(np_array, axis=1))
print("열방향 평균 : ", np.mean(np_array, axis=0))
print("행방향 평균 : ", np.mean(np_array, axis=1))
print("열방향 편차 : ", np.std(np_array, axis=0))
print("행방향 편차 : ", np.std(np_array, axis=1))
print("열방향 중위 : ", np.median(np_array, axis=0))
print("행방향 중위 : ", np.median(np_array, axis=1))
