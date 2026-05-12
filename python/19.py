class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # 1. Crear el nodo dummy para simplificar casos de borde
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    
    # 2. Mover el puntero fast n pasos adelante
    for _ in range(n):
        fast = fast.next
        
    # 3. Mover ambos hasta que fast llegue al final
    while fast.next:
        fast = fast.next
        slow = slow.next
        
    # 4. slow.next es el nodo a eliminar
    slow.next = slow.next.next
    
    return dummy.next
