class Solution {
    public boolean isPalindrome(String s) {
    String st = s.toLowerCase();
         s = st.replaceAll("[^a-zA-Z0-9]", "");
        String riv = new StringBuilder( s).reverse().toString();
        if(s.equals(riv)) return true;
        return false;       
    }
}
