class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set(["+", "-", "*", "/"])
        op_stack = []

        for token in tokens:
            if token not in operands:
                op_stack.append(token)
                print("Pushing: " + token)
            elif token in operands:
                rhs = op_stack.pop()
                lhs = op_stack.pop()
                print("Performing " + lhs + token + rhs)
                # Use int() on the result of division to truncate toward zero
                res = eval(lhs+token+rhs)
                op_stack.append(str(int(res)))
        return int(float(op_stack.pop()))