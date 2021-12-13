# Complete the 'commonPrefix' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY inputs as parameter.

def common_start(stra, strb):
    """ returns the longest common substring from the beginning of stra and strb """
    def _iter():
        for a, b in zip(stra, strb):
            if a == b:
                yield a
            else:
                return ""

    return ''.join(_iter())


def commonPrefix(inputs):
    # Write your code here
    input = inputs[0] # Consider the only string in the array inputs = ['abcabcd'] as example
    prefix_len_array = []
    len_sum = 0

    for i in range(len(input)):
      #prefix = input[:i]
      suffix = input[i:]
      common_str = common_start(input, suffix)
     
      if(common_str == ""): 
        prefix_len_array.append(0)
      else:
        len_sum += len(common_str)
        prefix_len_array.append(len(common_str))

    print ("The sum is ", len_sum)
    return prefix_len_array
#Test the function after removing the comment below
#print (commonPrefix(['abcabcd'])  )