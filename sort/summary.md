## 정렬 알고리즘

**정렬**이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다. 이번에 알아볼 정렬 방법은 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬을 알아보자.

## 선택 정렬

리스트 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하는 것이다.

```python
array = [4, 3, 2, 5, 1, 7]

for i in range(0, len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
```

## 삽입 정렬

삽입 정렬은 특정한 데이터를 적절한 위치에 삽입한다는 의미이다. 삽입 정렬의 특징은 ‘거의 정렬되어 있는 상태’를 정렬하는 것이 빠르다는 것이다.

```python
array = [3, 4, 2, 5, 1, 7]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
```

## 퀵 정렬

퀵 정렬에서는 피벗이 사용된다. 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준이다. 여기서는 첫 번째 데이터를 피벗으로 설정하였다.

처음부터 시작하는 방향과 끝부터 처음으로 가는 방향, 두 방향으로 피벗 기준으로 큰 값은 오른쪽으로 작은 값은 왼쪽으로 각각 배열에 추가한다.  피벗 기준으로 정렬이 완료되었으면 피벗을 각각 정렬된 배열 가운데 추가하고 각각 정렬된 배열의 첫 번째 데이터를 피벗으로 결정하고 이 과정을 반복한다. 

```python
array = [3, 4, 2, 5, 1, 7]

def quick_sort(array):
    if len(array) <= 1:
				#배열에 숫자 하나만 남았다면 배열 return
        return array
    
    pivot = array[0] #피벗
    tail = array[1:] #피벗을 제외한 리스트
    
    left = [num for num in tail if num < pivot] #피벗보다 작은 왼쪽 리스트
    right = [num for num in tail if num >= pivot] #피벗보다 큰 오른쪽 리스트
    
    return quick_sort(left) + [pivot] + quick_sort(right) #왼쪽리스트 + 피벗 + 오른쪽리스트

print(quick_sort(array))
```

## 계수 정렬

계수 정렬은 모든 범위를 담을 수 있는 크기의 리스트(배열)을 선언 할 수 있다면 빠른 정렬 알고리즘이다. 계수 정렬은 별도의 리스트를 선언하고 정렬하고자 하는 리스트의 값들을 새로 선언된 리스트의 인덱스로 사용하고 그 값 개수를 추가한다. 그리고 그 개수대로 출력하면 정렬이 되어있다.

```python
array = [3, 6, 4, 3, 8, 9, 2]
count = [0] * (max(array)+1)

for num in array:
    count[num] += 1

for i in range(len(count)):
    if count[i] == 0:
        continue
    for _ in range(count[i]):
        print(i, end=" ")
```

## Python의 정렬 라이브러리

### sorted(list) → list

`sorted` 는 정렬된 리스트를 반환한다. 

```python
array = [5, 4, 3, 2, 1]
s_array = sorted(array)
print(s_array) #1 2 3 4 5
```

### sorted key 활용

key 파라미터에 정렬하고자 하는 데이터를 반환하는 함수를 넣어주면 된다.

```python
array = [("lee", 27), ("kim", 32), ("nam", 11)]
s_array = sorted(array, key=lambda data: data[1])
print(s_array)
```