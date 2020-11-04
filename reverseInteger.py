class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x<0 else False
        version_str=str(x)[1:] if negative else str(x)
        version_str = version_str[::-1]
        x=-int(version_str) if negative else int(version_str)
        if x< -2**31 or x>(2**31)-1:
            return 0
        return x
        