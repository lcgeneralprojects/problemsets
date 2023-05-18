import unittest
from where_will_the_ball_fall import Solution


class MyTests(unittest.TestCase):

    # Cases are submitted in the format (input, expected_output
    cases = list()
    cases.append(([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]],
                 [1,-1,-1,-1,-1]))
    cases.append(([[-1]],
                  [-1]))
    cases.append(([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]],
                  [0,1,2,3,4,-1]))

    def test_something(self):
        for case, expected in self.cases:
            self.assertEqual(expected, Solution().findBall(case))

if __name__ == '__main__':
    unittest.main()
