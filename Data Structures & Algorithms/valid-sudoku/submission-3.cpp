class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();
        int m = board[0].size();

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                char num = board[i][j];

                if(num == '.') continue;
            
                for(int k = 0; k < n; k++){
                    if(k!=j && board[i][k] == num) return false;
                }

                for(int k = 0; k < m; k++){
                    if(k!=i && board[k][j] == num) return false;
                }

                int row = (i/3)*3;
                int col = (j/3)*3;
                for(int r = row; r < row+3; r++){
                    for(int c = col; c < col+3; c++){
                        if((r != i || c != j) && board[r][c] == num) return false;
                    }
                }
            }
        }
        return true;
    }
};
