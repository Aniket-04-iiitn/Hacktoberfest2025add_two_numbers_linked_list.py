class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


def add_two_numbers(l1, l2):
    carry = 0
    dummy = Node(0)
    current = dummy

    while l1 or l2:
        x = l1.data if l1 else 0
        y = l2.data if l2 else 0

        total = x + y + carry
        carry = total // 10
        current.next = Node(total % 10)
        current = current.next

        # ✅ Move pointers only if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # ✅ Handle leftover carry
    if carry > 0:
        current.next = Node(carry)

    return dummy.next


def print_list(head):
    while head:
        print(head.data, end=" → ")
        head = head.next
    print("None")


# Example
# 1st Number: 342 represented as 2 → 4 → 3
# 2nd Number: 465 represented as 5 → 6 → 4
a1 = Node(2)
a1.next = Node(4)
a1.next.next = Node(3)

b1 = Node(5)
b1.next = Node(6)
b1.next.next = Node(4)

result = add_two_numbers(a1, b1)
print_list(result)  # ✅ Expected Output: 7 → 0 → 8 → None
