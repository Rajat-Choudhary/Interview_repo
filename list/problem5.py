def count_occ(list):
    count = 0
    for i in list:
        if len(i) > 2 and i[0] == i[-1]:
                count +=1
    return count
if __name__ == "__main__":
    Sample_List = ['abc', 'xyz', 'aba', '1221']
    result = count_occ(Sample_List)
    print(result)

