#1
def count_matches(ls, value):
    if ls == []:
        return 0
    if ls[0] == value:
        return count_matches(ls[1:], value) + 1
    else:
        return count_matches(ls[1:], value)

if __name__ == "__main__":
    print(
        count_matches([0, 1, 0, 4, 2, 0], 0),
        count_matches(["a", "b", "c"], 1),
        count_matches([], "a")
    )

#2
def double_each(ls):
    if ls == []:
        return []
    return [ls[0]] * 2 + double_each(ls[1:])

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(
        double_each(nums),
        nums,
        double_each([])
    )

#3
def sums_to(nums, k):
    if nums == []:
        return k == 0
    return sums_to(nums[1:], k - nums[0])

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(
        sums_to(nums, 6),
        sums_to(nums, 5),
        sums_to([], 1)
    )

#4
def is_reverse(str1, str2):
    if str1 == str2 == "":
        return True
    elif str1 == "" or str2 == "":
        return False
    if str1[0] == str2[-1]:
        return is_reverse(str1[1:], str2[:-1])
    else:
        return False

if __name__ == "__main__":
    print(
        is_reverse("abc","cba"),
        is_reverse("abc","abc"),
        is_reverse("abc","dcba"),
        is_reverse("abc","cb"),
        is_reverse("","")
    )

#5
def sort_repeated(L):
    elements = set(L)
    result = []
    for i in elements:
        if L.count(i) > 1:
            result.append(i)
    return sorted(result)

if __name__ == "__main__":
    print(
        sort_repeated([1,2,3,2,1]),
        sort_repeated([1,2,3,2,2,4]),
        sort_repeated(list(range(100)))
    )

#6
def make_Dict_number_1(lst):    # get() not used
    elements = set(lst)
    result = {}
    for i in elements:
        result[i] = lst.count(i)
    return result

def make_Dict_number_2(lst):    # get() used
    result = {}
    for i in lst:
        if result.get(i) == None:
            result[i] = 1
        else:
            result[i] += 1
    return result

def most_Frequent_1(lst):   # get() not used
    elements = set(lst)
    maxcnt = 0
    maxelement = None
    for i in elements:
        curcnt = lst.count(i)
        if (curcnt > maxcnt):
            maxcnt = curcnt
            maxelement = i
    return maxelement

def most_Frequent_2(lst):   # get() used
    result = {}
    maxcnt = 0
    maxelement = None
    for i in lst:
        if result.get(i) == None:
            result[i] = 1
        else:
            result[i] += 1
        curcnt = result.get(i)
        if curcnt > maxcnt:
            maxcnt = curcnt
            maxelement = i
    return maxelement

if __name__ == "__main__":
    print (make_Dict_number_1([2,5,3,4,6,4,2,4,5]))
    print (make_Dict_number_2([2,5,3,4,6,4,2,4,5]))
    print (most_Frequent_1([2,5,3,4,6,4,2,4,5]))
    print (most_Frequent_2([2,5,3,4,6,4,2,4,5]))

#7
def histogram(d):
    elements = set(d.values())
    result = {}
    for i in elements:
        result[i] = list(d.values()).count(i)
    return result

if __name__ == "__main__":
    letters = {1: "a", 2: "b", 3:"a"}
    print(histogram(letters))
    letters = {1: "a", 2: "b", 3:"c"}
    print(histogram(letters))
    letters[4] = "a"
    letters[5] = "b"
    letters[6] = "a"
    print(histogram(letters))
