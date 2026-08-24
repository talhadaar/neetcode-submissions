class Solution:

    # eg = ["Hello", "World", "Im", "batman"]
    # encode(eg) = ['005xxxxx005xxxxx002xx006xxxxxx']

    def encode(self, strs: List[str]) -> str:
        # concat string with delim '#'
        strs_concat = ''
        for item in strs:
            # TODO encode(item)
            strs_concat = strs_concat + str(len(item)).zfill(3) + item
        print(strs_concat)
        return strs_concat
        
    def decode(self, s: str) -> List[str]:

        strs_split = []
        # separate items & decode
        i=0
        while i in range(0,len(s)):
            item_l = int(s[i:i+3])

            # TOFO decode(item)
            decoded_item = s[i+3:i+3+item_l]

            # reconstruct strs[]
            strs_split.append(decoded_item)

            # move i to next item
            i = i + 3 + item_l
            print(strs_split)

        print(strs_split)
        return strs_split


