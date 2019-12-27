def rabbit_hare(ll):
    even = ll.head
    odd = ll.head
    while even.next.next:
        odd = odd.next
        even = even.next.next
    return odd

ll1 = [5,4,3,2,1]

ll2 = [6,5,4,3,2,1]

rabbit_hare(ll1)

