impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut l = 0;
        let mut r = heights.len() - 1;
        let mut max = 0;

        while l < r {
            let area = min(heights[l], heights[r]) * (r - l) as i32;
            if area > max { max = area; }
            if heights[l] < heights[r] {
                l+=1
            } else {
                r-=1;
            }
        }
        return max;
    }
}
