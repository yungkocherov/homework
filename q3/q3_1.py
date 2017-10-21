class StackSkobochek:
    def __init__(self, string):
        self.string = string
        self.stack = ""

    def check1(self):
        for i in range(len(self.string)):
            if self.string[i] == "(" or self.string[i] == "{" or self.string[i] == "[":
                self.stack += self.string[i]
            elif self.string[i] == ")":
                if self.stack[len(self.stack) - 2] == "(":
                    self.stack = self.stack[:-2]
                else:
                    return "invalid combination"
            elif self.string[i] == "}":
                if self.stack[len(self.stack) - 2] == "{":
                    self.stack = self.stack[:-2]
                else:
                    return "invalid combination"
            elif self.string[i] == "]":
                if self.stack[len(self.stack) - 2] == "[":
                    self.stack = self.stack[:-2]
                else:
                    return "invalid combination"
        if self.stack == "":
            return "Valid combination"
        else:
            return "invalid combination"


str = input()
o = StackSkobochek(str)
print(o.check1())
