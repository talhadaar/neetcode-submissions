impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {

        // unequal strings cannot be anagrams
        if s.len() != t.len() { return false };

        let mut ss = s.into_bytes();
        let mut st = t.into_bytes();

        ss.sort_unstable();
        st.sort_unstable();

        ss == st
    }
}
