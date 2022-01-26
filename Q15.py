#연습문제 15-1 그래프 탐색
#그래프 탐색: 너비 우선 탐색
#입력: 그래프 g, 탐색 시작점 start
#출력: start에서 출발해 연결된 꼭짓점들을 출력

def bfs(g, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)
#그래프정보
g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

bfs(g, 1)