def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))


print(find_needle(['hay', 'junk', 'hay', 'hay',
      'moreJunk', 'needle', 'randomJunk']))
