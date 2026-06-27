impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut fset = std::collections::HashSet::new();

        for &num in &nums {
            if !fset.insert(num) {return true;}
        }
        return false;
    }
}
