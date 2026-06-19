use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {

        let mut row: Vec<HashSet<char>> = vec![HashSet::new();9];
        let mut col: Vec<HashSet<char>> = vec![HashSet::new(); 9];
        let mut sq: Vec<HashSet<char>> = vec![HashSet::new(); 9];

        for r in 0..9 {
            for c in 0..9 {
                if board[r][c] == '.' {
                    continue;
                }

                let cell = board[r][c];
                let sqid = (r/3)*3 + c / 3;

                if !row[r].insert(cell)
                    || !col[c].insert(cell)
                    || !sq[sqid].insert(cell) {
                        return false;
                }
            }
        }
    return true;
    }
}
