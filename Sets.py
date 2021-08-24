# QUESTION 1
def removeDuplicates(sequence):
    '''removeDuplicates() preserves only single instances of each value in the sequence
    
    arg
    -- sequence : list

    return
    -- list
    '''

    result = []
    for value in sequence:
        if value not in result:
            result.append(value)
        
    return result

print(removeDuplicates([1,2,2,3,3,3,4,5,6,7,7,7,8,8,9])) #(quadratic )


def removeDuplicates2(sequence):
    resultSet = set()

    for value in sequence:
        if value not in resultSet:
            resultSet.add(value)
    
    return list(resultSet)

print(removeDuplicates2([1,2,2,3,3,3,4,5,6,7,7,7,8,8,9]))

print()

# QUESTION 2
def isUnique(seq1, seq2):
    '''isUnique() determines if no values in seq1 occur in seq2
    
    arg
    -- seq1 : list
    -- seq2 : list
    
    return
    -- Boolean
    '''

    for item in seq1:
        if item in seq2:
            return False

    return True
#end of isUnique

def isUnique2(seq1, seq2):
    setSeq1 = set(seq1)
    setSeq2 = set(seq2)

    return setSeq1.isdisjoint(setSeq2)
# end of isUnique2

print()

# QUESTION 3
def complement(universe, aSet):
    '''complement() returns all the values that exist in the universe but not in aSet
    
    arg
    -- universe : set
    -- aSet: set
    
    return
    -- set
    '''
    
    '''
    result = set()

    for item in universe:
        if item not in aSet:
            result.add(item)

    return result
    '''

    return universe - aSet

print()

# QUESTION 4
evenSet = {x for x in range(1,100) if x % 2 == 0}
print('Even set:', evenSet)

print()

oddSet = set(range(1,100)) - evenSet
print('Odd set:', oddSet)

print()
print()

# QUESTION 6
setA = {0,1,2}
pSetA = []
val = 0

while val < len(setA):
    pSetA.append(val)
    val += 1

print(setA)