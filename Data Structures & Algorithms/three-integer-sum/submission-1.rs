impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {

        let mut sorted_nums = nums.clone();
        sorted_nums.sort_unstable();

        let sorted_nums_len = sorted_nums.len();

        let mut result = Vec::new();

        for i in 0..sorted_nums_len {

            let anchor = sorted_nums[i];

            // sorted_nums[n+1] are all > 0 so three_sum will always be > 0
            if anchor > 0 {
                break;
            }

            // skip duplicate num
            if i > 0 && anchor == sorted_nums[i - 1] {
                continue;
            }

            let mut l = i + 1;
            let mut r = sorted_nums_len - 1;
            let mut sum = 0;

            while l < r {
                sum = anchor + sorted_nums[l] + sorted_nums[r];

                if sum > 0 {
                    r-=1;
                } else if sum < 0 {
                    l+=1;
                } else if sum == 0 {
                    //record triplet
                    result.push(vec![anchor, sorted_nums[l], sorted_nums[r]]);
                    
                    // Skip duplicates for l and r
                    while l < r && sorted_nums[l] == sorted_nums[l + 1] { l += 1; }
                    while l < r && sorted_nums[r] == sorted_nums[r - 1] { r -= 1; }
                    
                    r-=1;
                    l+=1;
                }
            }
        }

        return result;
    }
}
