class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sorted_lists(head1, head2):
    dummy = Node()
    tail = dummy

    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    return dummy.next


def insertion_sort(head):
    dummy = Node()
    dummy.next = head
    sorted_tail = dummy.next
    unsorted_head = sorted_tail.next
    while unsorted_head:
        if unsorted_head.data < sorted_tail.data:
            sorted_prev = dummy
            while sorted_prev.next.data < unsorted_head.data:
                sorted_prev = sorted_prev.next
            sorted_tail.next = unsorted_head.next
            unsorted_head.next = sorted_prev.next
            sorted_prev.next = unsorted_head
            unsorted_head = sorted_tail.next
        else:
            sorted_tail = unsorted_head
            unsorted_head = unsorted_head.next
    return dummy.next


# Приклад використання
if __name__ == "__main__":
    # Створення вхідного однозв'язного списку
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(4)
    head.next.next.next = Node(2)

    print("Однозв'язний список до реверсування:")
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    # Реверсування однозв'язного списку
    head = reverse_linked_list(head)

    print("Однозв'язний список після реверсування:")
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    # Створення двох відсортованих однозв'язних списків
    list1 = Node(1)
    list1.next = Node(3)
    list1.next.next = Node(5)

    list2 = Node(2)
    list2.next = Node(4)
    list2.next.next = Node(6)

    print("Об'єднання двох відсортованих однозв'язних списків:")
    merged_head = merge_sorted_lists(list1, list2)
    current = merged_head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

    # Виконання сортування вставками
    head = insertion_sort(head)

    print("Однозв'язний список після сортування вставками:")
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
