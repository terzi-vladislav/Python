def insert_sort(A):
    """ Сортировка списка А вставками """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1

def choise_sort(A):
    """ Сортировка списка А выбором """
    N = len(A)
    for pos in range(N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
 
def bubble_sort(A):
    """ Сортировка списка А пузырьком """
    N = len(A)
    for bypass in range(1, N):
        for j in range(N - bypass):
            if A[j + 1] < A[j]:
                A[j + 1], A[j] = A[j], A[j + 1]
        

def test_sort(sort_algorythm):
    print('Тестируем: ', sort_algorythm.__doc__)
    print("testcase #1: ", end = "")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorythm(A)
    print("OK" if A == A_sorted else "Fail")
    
    print("testcase #2: ", end = "")
    A = list(range(10, 20)) + list(range(10))
    A_sorted = list(range(20))
    sort_algorythm(A)
    print("OK" if A == A_sorted else "Fail")
    
    print("testcase #3: ", end = "")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorythm(A)
    print("OK" if A == A_sorted else "Fail")
        
        
        
if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)