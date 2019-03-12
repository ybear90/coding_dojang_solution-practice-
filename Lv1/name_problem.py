name_str = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

# Question 1
cntKim = 0
cntLee = 0

name_list = name_str.split(",")
print(name_list[0])
print(name_list)
for name in name_list:
 if name[0] == "김":
  cntKim += 1
 elif name[0] == "이":
  cntLee += 1
print("="*30)
print("이: ", cntLee, "김: ", cntKim)

# Question 2
findLJY = 0

for name in name_list:
 if name == "이재영":
  findLJY += 1

print("="*30)
print("이재영의 갯수: ", findLJY)

# Question 3
name_only_list = set(name_list)
name_mod_list = list(name_only_list)

print("="*30)
("중복을 제거한 결과: ")
print(name_mod_list)

# Question 4
print("="*30)
name_mod_list.sort()
print(name_mod_list)
