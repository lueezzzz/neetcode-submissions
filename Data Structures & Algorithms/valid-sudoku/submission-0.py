class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[r])):

                if board[r][c] == ".":
                    continue

                row = (board[r][c], "row", r)
                col = (board[r][c], "col", c)
                bounding_box = (board[r][c], "bounding_box", r // 3, c //3 )

                if row in seen or col in seen or bounding_box in seen:
                    return False

                seen.add(row)
                seen.add(col)
                seen.add(bounding_box)

        return True