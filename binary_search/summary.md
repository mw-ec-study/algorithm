**”반으로 쪼개면서 탐색하기”**

이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다. 
이진 탐색은 탐색하고자 하는 범위의 시작점, 끝점, 중간점을 이용하여 탐색하며 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.

```python
def binary_search(array, target, start, end):
    if start >= end:
        return -1
    mid = (start + end)//2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid)
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)
```

### 코딩 테스트에서의 이진 탐색

이진 탐색의 원리는 다른 알고리즘에서도 폭넓게 적용되는 원리와 유사하기 때문에 매우 중요하다. 또, 높은 난이도의 문제에서는 이진 탐색 알고리즘이 다른 알고리즘과 함께 사용되기 때문에 코드를 외워두면 크게 도움이 된다.

## 떡볶이 떡 만들기

서로 길이가 다른 떡 여러 줄을 병렬적으로 나열해 놓고 한번에 길이 h로 자른다. 이때 손님이 원한 떡의 길이를 최소한으로 만족할 수 있는 h를 구하시오

### 소스코드

```python
#n: 떡의 개수, m: 요청한 떡의 길이
n, m = list(map(int, input().split(" ")))
#떡 배열
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while start <= end:
    total = 0 #자르고 남은 떡 길이 총합
    mid = (start + end)//2
    for rc in array:
        if rc > mid:
            total += rc - mid
    if total < m:
        end = mid
    elif total > m:
        answer = mid #현재 최소 길이 저장
        start = mid
    elif total == m:
        answer = mid
        break
    
print(answer)
```

### 아이디어

병렬로 놓아져 있는 떡의 중간을 한번에 자르고 자르고 남은 떡의 길이를 모두 더한다.

1. 더한 값이 요구한 길이보다 작을 경우
    
    더 잘라야 하므로 end 값을 mid로 둔다.
    
2. 더한 값이 요구한 길이보다 클 경우
    
    현재까지 최소값이므로 mid 길이가 최소 길이로 두고
    덜 잘라야하므로 start 값을 mid로 둔다.
    
3. 1, 2를 반복하여 최소값을 찾는다.