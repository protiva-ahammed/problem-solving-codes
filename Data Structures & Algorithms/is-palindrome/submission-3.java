class Solution {
    public boolean isPalindrome(String s) {
        String st = s.toLowerCase();
        s = st.replaceAll("[^a-zA-Z0-9]", "");
        st = new StringBuilder( s).reverse().toString();
        return (s.equals(st)) ;
    }
}
