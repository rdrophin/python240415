# 형식비교.py
# List 예제
my_list = [1, 2, 3, 4, 5]

# Tuple 예제
my_tuple = (1, 2, 3, 4, 5)

# Set 예제
my_set = {1, 2, 3, 4, 5}

# Dictionary 예제
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 각 자료형의 요소에 접근하기
print("List 요소에 접근:", my_list[0])
print("Tuple 요소에 접근:", my_tuple[0])
# Set은 인덱싱이 불가능하므로 생략
print("Dictionary 요소에 접근:", my_dict['a'])

# List의 장단점
list_example = [1, 2, 3, 4, 5]
print("List 예제:", list_example)
print("List의 장점: 가변(mutable), 순서가 있음(인덱싱 및 슬라이싱 가능)")
print("List의 단점: 검색 및 삽입/삭제 시간이 느림")

# Tuple의 장단점
tuple_example = (1, 2, 3, 4, 5)
print("Tuple 예제:", tuple_example)
print("Tuple의 장점: 불변(immutable), 메모리 효율적")
print("Tuple의 단점: 삽입/삭제가 불가능하고, 인덱싱 및 슬라이싱은 가능하지만 값 변경은 불가능")

# Set의 장단점
set_example = {1, 2, 3, 4, 5}
print("Set 예제:", set_example)
print("Set의 장점: 중복을 허용하지 않음, 합집합, 교집합, 차집합 등 집합 연산 가능")
print("Set의 단점: 순서가 없음(인덱싱 및 슬라이싱 불가능)")

# Dictionary의 장단점
dict_example = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Dictionary 예제:", dict_example)
print("Dictionary의 장점: 키-값 쌍으로 데이터 저장, 검색이 빠름")
print("Dictionary의 단점: 메모리 소모가 크고, 순서가 없음(인덱싱 및 슬라이싱 불가능)")
