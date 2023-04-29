def solution(skill, skill_trees):
    answer = 0
    cnt = 0
    flag = False
    
    for skill_tree in skill_trees:
        for target in skill_tree:
            if cnt == len(skill):
                break
            if target in skill[cnt + 1:]:
                flag = True
                break
            if target == skill[cnt]:
                cnt += 1
        if not flag:
            answer += 1
        else:
            flag = False
        cnt = 0
    return answer
