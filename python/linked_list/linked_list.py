class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self,head=None):
        self.head = head
        # ll head of 1
        # (1) -> (2) -> none
        # insert 3
        # (3) -> (1) -> (2) -> None
    def insert(self, value):
        node = Node(value) # will create a node of 3
        if self.head is not None:
           node.next = self.head
        # we say 3's next is the current head which is 1
        # we have to tell the link list that we have a new head
        self.head = node
    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    # had help from this website https://www.educative.io/edpresso/what-is-the-str-method-in-python and learned about the to string method and this one too https://stackoverflow.com/questions/20875150/how-to-fill-an-empty-string-which-has-already-been-created-in-python
    def __str__(self):
        current = self.head
        new_string = ''
        while current is not None:
            new_string = new_string + (f'{current.value}')
        print(new_string)



def merge_sorted(list1, list2):
  # if both lists are empty then merged list is also empty
  # if one of the lists is empty then other is the merged list
  if list1 == None:
    return list2
  elif list2 == None:
    return list1

  merged_head = None;
  if list1.data <= list2.data:
    merged_head = list1
    list1 = list1.next
  else:
    merged_head = list2
    list2 = list2.next

  merged_tail = merged_head

  while list1 != None and list2 != None:
    temp = None
    if list1.data <= list2.data:
      temp = list1
      list1 = list1.next
    else:
      temp = list2
      list2 = list2.next

    merged_tail.next = temp
    merged_tail = temp

  if list1 != None:
    merged_tail.next = list1
  elif list2 != None:
    merged_tail.next = list2

  return merged_head
