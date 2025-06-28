class Node:
    def __init__(self, course):
        self.course = course
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_course(self, course):
        new_node = Node(course)
        new_node.next = self.head
        self.head = new_node

    def display_courses(self):
        current = self.head
        while current:
            print(f"- {current.course.name}")
            current = current.next
