class Node:
    """
    Node 클래스
    - 양방향 연결 리스트의 각 노드를 나타냄.
    Args:
        data: 노드에 저장할 데이터.
    Attributes:
        data: 노드에 저장된 데이터.
        next: 다음 노드를 가리키는 포인터 (기본값은 None).
        prev: 이전 노드를 가리키는 포인터 (기본값은 None).
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # 다음 노드 초기화
        self.prev = None  # 이전 노드 초기화


class Dequeue:
    """
    Dequeue 클래스
    - 이중 연결 리스트를 기반으로 구현된 양방향 큐.
    Attributes:
        front: 큐의 앞쪽 노드를 가리킴.
        rear: 큐의 뒤쪽 노드를 가리킴.
        length: 큐에 포함된 노드의 개수.
    """
    def __init__(self):
        self.rear = None  # 큐의 뒤쪽 노드 초기화
        self.front = None  # 큐의 앞쪽 노드 초기화
        self.length = 0  # 큐 길이 초기화

    def insertFront(self, data):
        """
        큐의 앞쪽에 데이터를 삽입하는 메서드.
        Args:
            data: 큐에 삽입할 데이터.
        """
        if self.length == 0:  # 큐가 비어 있는 경우
            self.front = self.rear = Node(data)  # 노드 생성 후 front와 rear에 설정
        else:
            node = Node(data)  # 새 노드 생성
            n_node = self.front
            self.front.prev = node  # 기존 front 노드의 prev를 새 노드로 설정
            self.front = node  # front를 새 노드로 업데이트
            self.front.next = n_node  # 새 노드의 next를 기존 front로 설정
        self.length += 1  # 큐 길이 증가

    def deleteFront(self):
        """
        큐의 앞쪽 데이터를 제거하고 반환하는 메서드.
        Returns:
            제거된 데이터.
        """
        data = self.front.data  # 제거할 데이터 저장
        if self.front == self.rear:  # 큐에 노드가 하나만 있는 경우
            self.front = self.rear = None  # 큐를 비움
        else:
            self.front = self.front.next  # front를 다음 노드로 설정
            self.front.prev = None  # 새로운 front의 prev를 None으로 설정
        self.length -= 1  # 큐 길이 감소
        return data

    def insertRear(self, data):
        """
        큐의 뒤쪽에 데이터를 삽입하는 메서드.
        Args:
            data: 큐에 삽입할 데이터.
        """
        if self.length == 0:  # 큐가 비어 있는 경우
            self.front = self.rear = Node(data)  # 노드 생성 후 front와 rear에 설정
        else:
            node = Node(data)  # 새 노드 생성
            p_node = self.rear
            self.rear.next = node  # 기존 rear 노드의 next를 새 노드로 설정
            self.rear = node  # rear를 새 노드로 업데이트
            self.rear.prev = p_node  # 새 노드의 prev를 기존 rear로 설정
        self.length += 1  # 큐 길이 증가

    def deleteRear(self):
        """
        큐의 뒤쪽 데이터를 제거하고 반환하는 메서드.
        Returns:
            제거된 데이터.
        """
        data = self.rear.data  # 제거할 데이터 저장
        if self.front == self.rear:  # 큐에 노드가 하나만 있는 경우
            self.front = self.rear = None  # 큐를 비움
        else:
            self.rear = self.rear.prev  # rear를 이전 노드로 설정
            self.rear.next = None  # 새로운 rear의 next를 None으로 설정
        self.length -= 1  # 큐 길이 감소
        return data

    def is_empty(self):
        """
        큐가 비어 있는지 확인하는 메서드.
        Returns:
            True: 큐가 비어 있음.
            False: 큐에 데이터가 있음.
        """
        return self.front is None


if __name__ == "__main__":
    # Dequeue 클래스 테스트
    q = Dequeue()

    # 큐에 데이터 추가
    q.insertFront(3)
    q.insertFront(4)

    # 뒤쪽에서 데이터 제거
    a = q.deleteRear()
    print(a)  # 출력: 3