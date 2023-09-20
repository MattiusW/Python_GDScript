def main():
    rating = [4.5, 3.0, 5.0, 2.5, 4.0]
    emptyList = []
    testOne = countAverage(rating)
    print("Test one:", testOne)
    print("Test two: ", countAverage(emptyList))


def countAverage(ratingList):
    if len(ratingList) > 0:
        sum = 0
        number = len(ratingList)
        for i in ratingList:
            sum += i
        count = sum / number 
        return count
    else:
        print("Empty list nothing to count")
        return None

if __name__ == "__main__":
    main()
    