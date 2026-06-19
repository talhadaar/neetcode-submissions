impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {

        let mut row = vec![[false; 10];9];
        let mut col = vec![[false; 10];9];
        let mut sq = vec![[false; 10];9];

        for r in 0..9 {
            for c in 0..9 {
                let cell = board[r][c];

                if cell == '.' {
                    continue;
                }

                // convert cell char to int
                // ASCII CODE(char) - ASCII CODE(0)
                let val = (cell as u8 - b'0') as usize;

                // index for subsquares
                let sqid = (r/3)*3 + (c / 3);

                if row[r][val] || col[c][val] || sq[sqid][val]{
                    return false
                }

                row[r][val] = true;
                col[c][val] = true;
                sq[sqid][val] = true;
            }
        }
    return true;
    }
}
