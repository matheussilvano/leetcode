class Solution(object):
    def rotateString(self, string_inicial, goal):
        double_string_inicial = string_inicial + string_inicial

        if len(goal) != len(string_inicial):
            return False
        elif goal in double_string_inicial:
            return True
        else:
            return False
