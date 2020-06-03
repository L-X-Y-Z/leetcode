# -*- coding: utf-8 -*-
class Solution:
    def new21Game_permutation_count(self, N: int, K: int, W: int) -> float:
        # why this is wrong: every permutation has different probability
        if K - 1 + W <= N:
            return 1
        if K > N:
            return 0
        probability = [0] * (K + W)
        probability[0] = 1
        for i in range(K):
            for j in range(1, W+1):
                probability[i + j] += probability[i]
        total_K_W = sum(probability[K:])
        total_K_N = sum(probability[K:N+1])
        return total_K_N / total_K_W

    def new21Game_timeout(self, N: int, K: int, W: int) -> float:
        if K-1+W<=N:
            return 1
        if K > N:
            return 0
        probability = [0] * (K + W)
        probability[0] = 1
        for i in range(K):
            for j in range(1, W+1): # 1/W for every reach, so this loop can calculated in one go
                probability[i+j] += probability[i] / W
        return sum(probability[K:N+1])
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0: return 1
        if K-1+W<=N:
            return 1
        if K > N:
            return 0
        probability = [0] * (1+N)
        probability[0] = 1
        last_w_sum = 1
        for i in range(1,N+1):
            probability[i] = last_w_sum / W
            if i < K:
                last_w_sum += probability[i]
            if i >= W:
                last_w_sum -= probability[i - W]
        return sum(probability[K:N+1])

if __name__ == '__main__':
    # 0 <= K <= N <= 10000
    # 1 <= W <= 10000
    N = [10, 6, 21, 6]
    K = [1, 1, 17, 4]
    W = [10, 10, 10, 5]
    sol = Solution()
    for n,k,w in zip(N, K, W):
        print(sol.new21Game(n, k, w))