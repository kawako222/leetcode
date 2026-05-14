class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # 1. Crear el nodo dummy para empezar la nueva lista
    dummy = ListNode()
    current = dummy
    
    # 2. Recorrer ambas listas mientras ninguna sea nula
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        # Avanzar el puntero de la lista fusionada
        current = current.next
        
    # 3. Enganchar lo que quede de la lista que no se haya vaciado
    current.next = list1 if list1 else list2
    
    # Devolvemos dummy.next porque dummy es solo un nodo vacío inicial
    return dummy.next
