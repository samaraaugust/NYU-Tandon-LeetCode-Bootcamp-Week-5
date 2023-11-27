class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def checker(row, col, path, visited):
            if not (0 <= row < m) or not (0 <= col < n) or visited[row][col]:
                return

            path += board[row][col]
            visited[row][col] = True

            if path in wordSet:
                foundW.add(path)

            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + i, col + j
                checker(new_row, new_col, path, visited)

            visited[row][col] = False

        m, n = len(board), len(board[0])
        wordSet = set(words)
        foundW = set()

        for i in range(m):
            for j in range(n):
                checker(i, j, '', [[False] * n for _ in range(m)])

        return list(foundW)
