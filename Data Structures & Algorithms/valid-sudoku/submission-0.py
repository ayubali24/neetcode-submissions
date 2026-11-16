class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            tracker = set()
            for val in row:
                if val != "." and val in tracker:
                    return False
                elif val != "." and val not in tracker:
                    tracker.add(val)
        
        for col in zip(*board):
            tracker = set()
            for val in col:
                if val != "." and val in tracker:
                    return False
                elif val != "." and val not in tracker:
                    tracker.add(val)
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                tracker = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]
                        if val != "." and val in tracker:
                            return False
                        elif val != "." and val not in tracker:
                            tracker.add(val)
        

        return True