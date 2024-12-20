class Node:
    """
    Node 클래스
    - 단일 노드를 나타내는 클래스.
    
    Args:
        data: 노드에 저장할 데이터.
    
    Attributes:
        data: 노드에 저장된 데이터.
        next: 다음 노드를 가리키는 포인터(기본값은 None).
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # 초기화 시 다음 노드는 None으로 설정

class Linked_list:
    """
    단일 연결 리스트(Linked List) 구현 클래스.
    
    Attributes:
        head: 리스트의 첫 번째 노드를 가리키는 포인터.
        tail: 리스트의 마지막 노드를 가리키는 포인터.
        length: 리스트에 포함된 노드의 개수.
    """
    def __init__(self):
        self.head = None  # 리스트의 시작점
        self.tail = None  # 리스트의 끝점
        self.length = 0   # 초기 길이는 0

    def __len__(self):
        """
        len() 함수를 통해 리스트의 길이를 반환.
        Returns:
            리스트의 노드 개수(length).
        """
        return self.length

    def initialize_node(self, data):
        """
        head와 tail을 초기화하는 메서드.
        - 리스트가 비어 있는 상태에서 첫 번째 노드를 추가할 때 사용.
        
        Args:
            data: 초기화할 노드의 데이터.
        """
        self.head = Node(data)
        self.tail = self.head  # 첫 번째 노드는 head와 tail이 동일

    def append_list(self, data):
        """
        리스트의 끝에 데이터를 추가하는 메서드.
        
        Args:
            data: 추가할 데이터.
        """
        if self.head is None:  # 리스트가 비어 있는 경우
            self.initialize_node(data)
        else:  # 리스트가 비어 있지 않은 경우
            self.tail.next = Node(data)  # 현재 tail의 next를 새로운 노드로 설정
            self.tail = self.tail.next  # tail을 새로운 노드로 업데이트
        self.length += 1  # 리스트 길이 증가

    def append_list_left(self, data):
        """
        리스트의 앞(head) 부분에 데이터를 추가하는 메서드.
        
        Args:
            data: 추가할 데이터.
        """
        if self.head is None:  # 리스트가 비어 있는 경우
            self.initialize_node(data)
        else:
            node = Node(data)  # 새 노드 생성
            node.next = self.head  # 새 노드의 다음을 기존 head로 설정
            self.head = node  # head를 새 노드로 업데이트
        self.length += 1  # 리스트 길이 증가

    def show_list(self):
        """
        리스트의 모든 노드를 출력하는 메서드.
        """
        point = self.head  # 현재 노드 포인터를 head로 설정
        i = 0  # 인덱스 초기화
        while point is not None:  # 노드가 존재할 때까지 반복
            print(i, point.data)  # 인덱스와 노드 데이터 출력
            point = point.next  # 다음 노드로 이동
            i += 1

    def del_index(self, index):
        """
        특정 인덱스에 위치한 노드를 삭제하는 메서드.
        
        Args:
            index: 삭제할 노드의 인덱스.
        """
        if index < 0 or index >= self.length:  # 유효하지 않은 인덱스
            print("Invalid index")
            return
        
        if self.length == 1:  # 리스트에 노드가 하나만 있을 경우
            self.head = None
            self.tail = None
            self.length -= 1
            print("complete delete")
            return 
        
        if index == 0:  # 첫 번째 노드를 삭제하는 경우
            self.head = self.head.next  # head를 다음 노드로 설정
            self.length -= 1
            print("complete delete")
            return
        
        # 삭제할 노드 이전의 노드를 찾기
        point = self.head
        for i in range(0, index - 1):
            point = point.next
        
        point.next = point.next.next  # 삭제할 노드를 건너뛰도록 설정
        if point.next is None:  # 삭제 후 tail을 업데이트
            self.tail = point
        self.length -= 1
        print("complete delete")

    def del_data(self, data):
        """
        특정 데이터를 가진 노드를 삭제하는 메서드.
        
        Args:
            data: 삭제할 노드의 데이터.
        """
        if self.head is None:  # 리스트가 비어 있는 경우
            print("Data not found")
            return
        
        if self.head.data == data:  # head 노드가 삭제 대상인 경우
            self.head = self.head.next
            self.length -= 1
            print("complete delete")
            return 
        
        # 삭제할 노드를 탐색
        point = self.head.next
        prev = self.head

        while point is not None:
            if point.data == data:  # 삭제할 노드를 찾은 경우
                prev.next = point.next  # 이전 노드의 next를 업데이트
                if point.next is None:  # 삭제 대상이 tail인 경우
                    self.tail = prev
                self.length -= 1
                print("complete delete")
                return
            prev = point
            point = point.next

        print("Data not found")  # 데이터를 찾지 못한 경우

if __name__ == "__main__":
    # 연결 리스트 테스트
    my_list = Linked_list()
    my_list.append_list(1)
    my_list.append_list(2)
    my_list.append_list(3)
    my_list.append_list(4)
    my_list.show_list()  # 리스트 출력
    my_list.del_index(0)  # 인덱스로 삭제
    my_list.del_data(4)  # 데이터로 삭제
    my_list.show_list()  # 삭제 후 리스트 출력
    print(len(my_list))  # 리스트 길이 출력
