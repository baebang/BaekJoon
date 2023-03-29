import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
orders = list(map(int, input().split()))

multitap = []
count = 0

for i, current_device in enumerate(orders):
    # 1. 지금 사용할 전자제품이 이미 멀티탭에 꽂혀있다면 skip
    if current_device in multitap:
        continue

    # 2. 멀티탭에 여유 플러그가 아직 남아있으면 삽입
    elif len(multitap) < N:
        multitap.append(current_device)
        continue
        
    # 3. 멀티탭에 공간이 없을 경우
    else:
        candidate_del_multitap_index = 0
        max_index = 0

        for j, using_device in enumerate(multitap):
            # 1) 멀티탭에 꽂혀있는 전자제품 중 이후에 사용하는 것이 없는 경우
            # 사용하지 않는 제품 빼고 새 제품 꽂는다
            if using_device not in orders[i + 1:]:
                candidate_del_multitap_index = j
                break

            # 2) 멀티탭에 꽂혀있는 모든 전기용품들이 이후에도 사용되는 경우
            # 멀티탭에 꽂혀있는 전자제품 중 가장 나중에 사용하는 전자제품 뽑고 새로운 전자제품 꽂는다   
            else:
                if orders[i + 1:].index(using_device) > max_index:
                    candidate_del_multitap_index = j
                    max_index = orders[i + 1:].index(using_device)

        del multitap[candidate_del_multitap_index]
        multitap.append(current_device)
        count += 1

print(count)