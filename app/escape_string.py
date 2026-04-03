class EscapeString:
    def __init__(self, arg=""):
        self._escape_op = chr(92)  # backslash
        if isinstance(arg, str):
            self._chars = list(arg)
        else:
            raise Exception("Argument must be a string.")

        self._escaped = {}
        self._parse()

    def _parse(self):
        for i, char in enumerate(self._chars):
            if self._is_escaped(i):
                self._escaped[i] = {"chr": char, "is_escaped": True}
            else:
                if char != self._escape_op:
                    self._escaped[i] = {"chr": char, "is_escaped": False}

    def _is_escaped(self, i):
        c = self._count_escape_chars(i)
        return c % 2 != 0

    def _count_escape_chars(self, i):
        pi = i - 1
        c = 0
        while pi >= 0:
            if self._chars[pi] != self._escape_op:
                break
            c += 1
            pi -= 1
        return c

    def get_escaped(self):
        return self._escaped

    def get_escape_chr(self):
        return self._escape_op
