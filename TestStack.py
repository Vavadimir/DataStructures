import unittest
import Stack as s

class Tests(unittest.TestCase):

    def test_push(self):
        colors = s.Stack()
        colors.push("Pthalo Blue")
        assert colors.count() == 1
        colors.push("Ultramarine Blue")
        assert colors.count() == 2

    def test_pop(self):
        colors = s.Stack()
        colors.push("Magenta")
        colors.push("Alizarin")
        assert colors.pop() == "Alizarin"
        assert colors.pop() == "Magenta"
        assert colors.pop() == None

    def test_last(self):
        colors = s.Stack()
        colors.push("Cadmium Red Light")
        assert colors.top() == "Cadmium Red Light"
        colors.push("Hansa Yellow")
        assert colors.top() == "Hansa Yellow"

if __name__ == '__main__':
    unittest.main()