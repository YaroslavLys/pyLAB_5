import re


def main():
    input_file = "D:\\Python\\PycharmProjects\\access_log_Jul95"

    with open(input_file, mode="r") as f:
        result1 = re.findall(r"\[01/Jul/1995:01:39:\d\d -0400] \"GET /shuttle/missions/sts-\d\d", f.read())
    with open(input_file, mode="r") as f:
        result2 = re.findall(r"\[01/Jul/1995:01:[4-5]\d:\d\d -0400] \"GET /shuttle/missions/sts-\d\d", f.read())
    with open(input_file, mode="r") as f:
        result3 = re.findall(r"\[01/Jul/1995:02:\d\d:\d\d -0400] \"GET /shuttle/missions/sts-\d\d", f.read())
    with open(input_file, mode="r") as f:
        result4 = re.findall(r"\[01/Jul/1995:03:[0-3]\d:\d\d -0400] \"GET /shuttle/missions/sts-\d\d", f.read())
    with open(input_file, mode="r") as f:
        result5 = re.findall(r"\[01/Jul/1995:03:4[0-2]:\d\d -0400] \"GET /shuttle/missions/sts-\d\d", f.read())

    result = []
    result.extend(result1)
    result.extend(result2)
    result.extend(result3)
    result.extend(result4)
    result.extend(result5)

    missions = set()
    for item in result:
        print(item)
        missions.add(item[-6:])

    list_of_missions = list(missions)
    list_of_missions.sort(key=lambda x: int(x[-2:]), reverse=False)
    print("----- List of unique missions -----")
    for item in list_of_missions:
        print(item)


if __name__ == '__main__':
    main()
