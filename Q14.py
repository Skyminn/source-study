#연습문제 14-1 딕셔너리로 학생 번호에 해당하는 학생 이름 찾기
def find_name(sample_info, num):
    if num in sample_info:
        return sample_info[num]
    else:
        return "?"

sample_info = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(find_name(sample_info, 39))
print(find_name(sample_info, 67))
print(find_name(sample_info, 37))
