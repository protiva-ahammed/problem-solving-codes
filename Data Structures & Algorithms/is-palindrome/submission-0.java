class Solution {
    public boolean isPalindrome(String s) {
String st = s.toLowerCase();
        String s1 = st.replaceAll("[^a-zA-Z0-9]", "");
        String riv = new StringBuilder( s1).reverse().toString();
        if(s1.equals(riv)) return true;
        return false;       
    }
}
