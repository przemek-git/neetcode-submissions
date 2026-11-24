class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(s, e):
            if e - s + 1 <= 1: 
                return

            pivot = pairs[e].key
            swap_ptr = s
            for i in range(s, e):
                if pairs[i].key < pivot:
                    pairs[swap_ptr], pairs[i] = pairs[i], pairs[swap_ptr]
                    swap_ptr += 1

            pairs[swap_ptr], pairs[e] = pairs[e], pairs[swap_ptr]
            
            sort(s, swap_ptr - 1)
            sort(swap_ptr + 1, e)

        sort(0, len(pairs) - 1)
        return pairs