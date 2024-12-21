class Node:
    """
    Node 클래스
    - 스택의 각 노드를 나타냄.
    Args:
        data: 노드에 저장할 데이터.
    Attributes:
        data: 노드에 저장된 데이터.
        next: 다음 노드를 가리키는 포인터(기본값은 None).
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # 다음 노드 초기화

class Stack:
    """
    Stack 클래스
    - 연결 리스트 기반 스택 구현.
    Attributes:
        top: 스택의 최상단 노드를 가리킴.
        length: 스택에 포함된 노드의 개수.
    """
    def __init__(self):
        self.top = None  # 스택의 최상단 노드 초기화
        self.length = 0  # 스택 길이 초기화

    def stack_push(self, data):
        """
        스택에 데이터를 추가하는 메서드 (Push 연산).
        Args:
            data: 스택에 추가할 데이터.
        """
        new_node = Node(data)  # 새 노드 생성
        new_node.next = self.top  # 새 노드의 다음 노드를 기존 top으로 설정
        self.top = new_node  # top을 새 노드로 업데이트
        self.length += 1  # 스택 길이 증가

    def stack_pop(self):
        """
        스택의 최상단 데이터를 제거하고 반환하는 메서드 (Pop 연산).
        Returns:
            제거된 데이터 (최상단 데이터). 스택이 비어 있으면 0 반환.
        """
        if self.length == 0:  # 스택이 비어 있는 경우
            print("Invalid operation: Stack is empty")
            return 0
        else:
            p_data = self.top.data  # 최상단 데이터 저장
            self.top = self.top.next  # top을 다음 노드로 설정
            self.length -= 1  # 스택 길이 감소
            return p_data

    def stack_peek(self):
        """
        스택의 최상단 데이터를 확인하는 메서드 (제거하지 않음).
        Returns:
            최상단 데이터. 스택이 비어 있으면 None 반환.
        """
        if self.length == 0:  # 스택이 비어 있는 경우
            print("Invalid operation: Stack is empty")
            return None
        else:
            return self.top.data

    def is_Empty(self):
        """
        스택이 비어 있는지 확인하는 메서드.
        Returns:
            True: 스택이 비어 있음.
            False: 스택에 데이터가 있음.
        """
        return self.length != 0

if __name__ == "__main__":
    # 스택 클래스 테스트
    my_Stack = Stack()

    # 스택에 데이터 추가 (Push)
    my_Stack.stack_push(3)
    my_Stack.stack_push(5)
    my_Stack.stack_push(7)

    # 최상단 데이터 확인 (Peek)
    print("Top element (peek):", my_Stack.stack_peek())

    # 스택에서 데이터 제거 (Pop)
    num = my_Stack.stack_pop()
    print("Popped element:", num)

    # 스택이 비어 있는지 확인
    empty = my_Stack.is_Empty()
    print("Is stack empty?:", empty)

    # 최종 스택 상태 확인
    print("Remaining top element:", my_Stack.stack_peek())
    print("Stack length:", my_Stack.length)
