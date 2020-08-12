# 힙 : 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리

# 힙을 사용하는 이유
# 배열에 데이터를 넣고 최대값, 최소값을 찾는 경우 -> O(n)
# 힙에 데이터를 넣고 최대값, 최소값을 찾는 경우 -> O(log(n))
# 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야하는 경우에 요긴하게 쓰임

# 힙의 두가지 조건
# 1. 최대힙에서 루트노드는 가장 큰 수이고, 최소힙에서 루트노드는 가장 작은 수이다. 
# 2. 완전이진트리이다. 완전 이진 트리는 가장 왼쪽 자식노드부터 채워진다.

# 힙과 이진탐색트리의 공통점과 차이점
# 공통점
# 모두 이진 트리이다.

#차이점
# 힙은 부모노드가 가장 크거나 혹은 작지만
# 이진탐색트리는 가장 왼쪽에 있는 노드가 가장 작고, 가장 오른쪽에 있는 노드가 가장 크다.
# 따라서, 힙은 오로지 최대 혹은 최소값을 빠르게 찾기 위한 구조이고
# 이진탐색트리는 탐색을 위한 구조이다.


