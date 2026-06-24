class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();
        int m = board[0].size();

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == '.') continue;

                char num = board[i][j];
                for(int k = 0; k < n; k++){
                    if(k == j) continue;
                    if(board[i][k] == num){
                        return false;
                    }
                }

                for (int k = 0; k < m; k++){
                    if(k == i) continue;
                    if(board[k][j] == num){
                        return false;
                    }
                }

                int boxRow = (i / 3) * 3;
                int boxCol = (j / 3) * 3;
                for(int r = boxRow; r < boxRow + 3; r++){
                    for(int c = boxCol; c < boxCol + 3; c++){
                        if(r == i && c == j) continue; 
                        if(board[r][c] == num) return false;
                    }
                }
            }
        }
        return true;
    }
};
