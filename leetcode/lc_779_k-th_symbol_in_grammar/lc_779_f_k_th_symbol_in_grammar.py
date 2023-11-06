class Solution:
    def kthGrammar(self, n, k):
        # The result depends on the parity of the number of times that we have to go to the 'right' half of the
        # current segment of the sequence when bisecting the current segment a la binary search
        # For example, for n = 3 we have the sequence '0110'; for k = 4, we go to the right half and get the new
        # segment '10', and then do that again and get the single-character segment '0' Similarly, for n = 3, k = 3,
        # we go '0110' -(right)-> '10' -(left)-> '1'
        res = 0
        segment_length = 2**(n-1)

        while segment_length > 1:
            segment_length = segment_length // 2

            if k > segment_length:
                res = (1 - res) % 2
                k -= segment_length

        return res
