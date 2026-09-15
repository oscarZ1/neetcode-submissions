class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(9): 
            arr = [] 
            for j in range(9): 
                if board[i][j] != ".": 
                    arr.append(board[i][j])
            arr_set = set(arr)
            if len(arr) != len(arr_set): 
                return False 
        
        # column check 
        for i in range(9): 
            arr = []
            for j in range(9): 
                if board[j][i] != ".": 
                    arr.append(board[j][i]) 
            arr_set = set(arr)
            if len(arr) != len(arr_set): 
                return False 
        
        # 3x3 check 
        for start_row in (0, 3, 6):
            for start_col in (0, 3, 6):
                seen = set()
                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        val = board[r][c]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val) 
                

        return True

                
            
        
