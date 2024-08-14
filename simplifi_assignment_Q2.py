def minimum_shots_to_clear_view(T, test_cases):
    results = []
    for i in range(T):
        N, K = test_cases[i][0]
        heights = test_cases[i][1]
        count = sum(1 for height in heights if height > K)
        results.append(count)
    
    return results


T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    test_cases.append(((N, K), heights))

results = minimum_shots_to_clear_view(T, test_cases)

for result in results:
    print(result)


