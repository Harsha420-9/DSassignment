class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_zero_sum(self):
        dummy = Node(0)
        dummy.next = self.head
        prefix_sum = 0
        prefix_sum_map = {}
        current = dummy
        while current:
            prefix_sum += current.data
            if prefix_sum in prefix_sum_map:
                prev = prefix_sum_map[prefix_sum]
                prev.next = current.next
            else:
                prefix_sum_map[prefix_sum] = current
            current = current.next

        self.head = dummy.next

    def reverse_in_groups(self, head, k):
        current = head
        prev = None
        count = 0
        while current and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1
        if next_node:
            head.next = self.reverse_in_groups(next_node, k)
        return prev

    def merge_alternate(self, head1, head2):
        current1, current2 = head1, head2
        while current1 and current2:
            next1, next2 = current1.next, current2.next
            current2.next = next1
            current1.next = current2
            current1, current2 = next1, next2
        if current2:
            current1.next = current2

    def count_pairs_with_sum(self, arr, target_sum):
        seen = set()
        count = 0
        for num in arr:
            complement = target_sum - num
            if complement in seen:
                count += 1
            seen.add(num)
        return count

    def find_duplicates(self, arr):
        seen = set()
        duplicates = []
        for num in arr:
            if num in seen:
                duplicates.append(num)
            seen.add(num)
        return duplicates

    def kth_largest_smallest(self, arr, k):
        arr.sort()
        kth_largest = arr[-k]
        kth_smallest = arr[k - 1]
        return kth_largest, kth_smallest

    def move_negatives(self, arr):
        n = len(arr)
        neg_idx = 0
        for i in range(n):
            if arr[i] < 0:
                arr[i], arr[neg_idx] = arr[neg_idx], arr[i]
                neg_idx += 1

    def reverse_string_with_stack(self, s):
        stack = []
        for char in s:
            stack.append(char)
        reversed_str = ''
        while stack:
            reversed_str += stack.pop()
        return reversed_str

    def evaluate_postfix_expression(self, expression):
        stack = []
        operators = set(['+', '-', '*', '/'])
        for token in expression:
            if token not in operators:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    stack.append(op1 / op2)
        return stack[0]

class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(-1)
    linked_list.insert(4)
    linked_list.insert(-3)
    linked_list.insert(2)

    # 1. Delete elements in the linked list whose sum is equal to zero
    linked_list.delete_zero_sum()
    linked_list.display()

    # 2. Reverse a linked list in groups of given size
    linked_list.head = linked_list.reverse_in_groups(linked_list.head, 2)
    linked_list.display()

    # Create another linked list
    linked_list2 = LinkedList()
    linked_list2.insert(10)
    linked_list2.insert(20)
    linked_list2.insert(30)

    # 3. Merge a linked list into another linked list at alternate positions
    linked_list.merge_alternate(linked_list.head, linked_list2.head)
    linked_list.display()

    # 4. Count pairs with given sum in an array
    arr = [1, 5, 7, -1, 5]
    target_sum = 6
    print(linked_list.count_pairs_with_sum(arr, target_sum))

    # 5. Find duplicates in an array
    arr = [1, 2, 3, 3, 4, 5, 5, 6]
    print(linked_list.find_duplicates(arr))

    # 6. Find the Kth largest and Kth smallest number in an array
    arr = [10, 20, 30, 40, 50]
    k = 3
    print(linked_list.kth_largest_smallest(arr, k))

    # 7. Move all the negative elements to one side of the array
    arr = [1, -1, 3, 2, -7, -5, 11, 6]
    linked_list.move_negatives(arr)
    print(arr)
    # 8. Reverse a string using a stack data structure
    s = "hello"
    print(linked_list.reverse_string_with_stack(s))

    # 9. Evaluate a postfix expression using stack
    expression = "82+3-"
    print(linked_list.evaluate_postfix_expression(expression))  

    # 10. Implement a queue using the stack data structure
    queue = QueueUsingStack()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  
    print(queue.dequeue())  
    print(queue.dequeue())