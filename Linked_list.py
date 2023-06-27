# We have two classes here, one is Node which represents an individual element in the linked list. It has two class variables, one is data and next
# next is the pointer to the next element, the data is the value of the element that can contain integers, strings, boolean, etc. 
# The second class is the LinkedList class where you need a head variable which points to the head of the linkedlist.
# 
# 
# 

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # 1) First we will make a method called insert_at_beggining, It will take a data value and insert it at the beginning of the linked list
    def insert_at_beggining(self, value):
        element_of_the_linked_list = Node(data=value, next=self.head)
        self.head = element_of_the_linked_list

    # 2) define a print function for utility purposes
    def print_it(self):
        if self.head is None:
            print('This linked list is empty')
            return
        
        iterator = self.head
        linked_list_string = ''
        while iterator:
            linked_list_string += str(iterator.data) + '--->'
            iterator = iterator.next
            #  The above thing makes sense beacause self.head = element_of_the_list which is an object of the Node class, so self.head is an object of the node class and self.head.next is the class variable of the Node class.
        print(linked_list_string)

    # 3) Now we will make a method to insert element at the end
    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(data=value, next=None)
            # Here the next is None because at the end there is nothing to link or refer to after that
            return
        # but if the linked list is not empty, then we must iterate to the end and at the end we must insert this elemnrt or node
        iterator = self.head
        while iterator.next:    #i.e. if iterator.next does not exist then this node is the last node and we can change the next of this node and add insert our node after that at the end.
            iterator = iterator.next
        # After getting out of the while loop you are at the last element
        iterator.next = Node(data=value, next=None) 
        #  Very clever


    # 4) This method will take a list of values and create a new fresh linked list from it, the old linked list created will be discarded
    def list_to_linkedlist(self, list_of_values):
        self.head = None
        # This will replace Node object with None so the .data and .next will not work, hence all the list has been wiped out.
        # If you ask what happens to the objects we created , the those are all collected by the python garbage collector automatically. In any other language we would have to do it manually but pyhton has an edge here.
        for values in list_of_values:
            self.insert_at_end(values)

        
    # 5) This method will return the length of the linked list
    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
        
        return count
    
    # 6) This method will remove the element at a given index
    def remove_at(self, index_given):
        if index_given<0 or index_given>self.get_length():
            raise Exception('INDEX OUT OF BOUNDS.')
        if index_given == 0:
            self.head = self.head.next    # This shows an error but it runs as it is logically correct.
            return
        count = 0
        iterator = self.head
        while iterator:
            
            if count == index_given-1:    # Here we are at the element prior to the element we want to remove.
                iterator.next = iterator.next.next
                break # even if we did not break the loop the method will logically still work, but we break this loop to reduce the time complexity
                      # I mean once the work is done there is no point to iterate the linked list uselesly.
            
            iterator = iterator.next
            count += 1  # count must be given here because otherwise it will interfere with the program.

    

    # 7) This method will inset a element at the given index
    def insert_at(self, index_given, value):
        if index_given<0 or index_given>self.get_length():
            raise Exception('INDEX OUT OF BOUNDS.') 

        if index_given == 0:
            self.insert_at_beggining(value)
            return
        
        count = 0
        iterator = self.head
        while self.head:
            if count == index_given-1:  #Here we are at the element prior to the element we want to inserrt the new element at. 
                iterator.next = Node(data=value, next=iterator.next)

                # do the above step by step to remove confusion
                # element =  Node(data=value, next=iterator.next)
                # iterator.next = element
                # Above two lines sir did are the same thing i did in one line
                break # To reduce time complexity
            iterator = iterator.next
            count += 1





        






if __name__ == '__main__':

    #Unhash the hashed code to understand deeply about the links, it will show an error in the VS code but it will run properly. 
    # print(25*'*'+'Operation'+25*'*')
    Object_linked_list = LinkedList()
    print(Object_linked_list.head)
    # print(25*'*'+'Operation'+25*'*')
    Object_linked_list.insert_at_beggining(65)
    # print(Object_linked_list.head)
    # print(Object_linked_list.head.data)
    # print(Object_linked_list.head.next)
    # print(25*'*'+'Operation'+25*'*')
    Object_linked_list.insert_at_beggining(54)
    # print(Object_linked_list.head)
    # print(Object_linked_list.head.data)
    # print(Object_linked_list.head.next)
    # print(25*'*'+'Operation'+25*'*')
    Object_linked_list.print_it()
    # print(Object_linked_list.head)
    # print(Object_linked_list.head.data)
    # print(Object_linked_list.head.next)
    # print(25*'*'+'Operation'+25*'*')
    Object_linked_list.insert_at_end(12)
    # print(Object_linked_list.head)
    # print(Object_linked_list.head.data)
    # print(Object_linked_list.head.next)
    # print(25*'*'+'Operation'+25*'*')
    Object_linked_list.insert_at_end(5)
    # print(Object_linked_list.head)
    # print(Object_linked_list.head.data)
    # print(Object_linked_list.head.next)
    # print(25*'*'+'Operation'+25*'*')
    Object_linked_list.print_it()

    Object_linked_list.list_to_linkedlist(['banana', 'mangoes', 'grapes', 'orange'])
    Object_linked_list.print_it()
    length = Object_linked_list.get_length()
    print(length)
    Object_linked_list.remove_at(2)
    Object_linked_list.print_it()
    Object_linked_list.insert_at(2, 'blueberries')
    Object_linked_list.print_it()
    Object_linked_list.insert_at(0, 'figs')
    Object_linked_list.print_it()