impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        // alphabets only
        let chars: Vec<char> = s.chars().filter(|c| c.is_ascii_alphanumeric()).map(|c| c.to_ascii_lowercase()).collect();
        if chars.is_empty() {
            return true
        }

        let mut l = 0;
        let mut r = chars.len() - 1;
        
        while l < r {
            if chars[l] == chars[r] {
                l+=1;
                r-=1;
            } else {
                return false
            }
        }
    return true
    }
}
