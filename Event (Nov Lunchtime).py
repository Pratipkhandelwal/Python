DAYS = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7,
}

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        input_string = input()
        first_day, last_day, l, r = input_string.split()
        l = int(l)
        r = int(r)
        first_day = DAYS.get(first_day)
        last_day = DAYS.get(last_day)
        gap = last_day - first_day
        if gap < 0:
            min_days = 7 - abs(gap) + 1
        else:
            min_days = gap + 1
        # print(">>>>>>> ", min_days)
        count = 0
        # print(min_days)
        while min_days <= r:
            if min_days in range(l, r+1):
                # print("hehe")
                count += 1
            if count == 1:
                rem = min_days
            min_days += 7
        if count == 0:
            print("impossible")
        elif count == 1:
            print(rem)
        else:
            print("many")
