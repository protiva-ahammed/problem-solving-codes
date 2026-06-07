class Solution {
     public static boolean isPalindrome(String s){
        int l=0, r =s.length()-1;

        while(l < r){
            while(l < r && !isAlphaNum(s.charAt(l))){
                l++;
            }
            while((r > l) && !isAlphaNum(s.charAt(r))){
                r--;
            }
            if(Character.toLowerCase(s.charAt(l))!=Character.toLowerCase(s.charAt(r)))
                return false;
            l++;
            r--;
        }
        return true;
    }
    public static boolean isAlphaNum(char c){
        boolean b = (c >= 'A' && c <= 'Z') ||
                (c >= 'a' && c <= 'z') ||
                (c >= '0' && c <= '9');
        return b;
    }
}
