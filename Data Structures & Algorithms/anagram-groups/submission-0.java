class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String , List<String>> res = new HashMap<>();
        for(String s: strs){
            int [] count = new int[26];
            for(char c: s.toCharArray()){
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            // initializing the res with new keys and assign an array list so not get the null
            res.putIfAbsent(key , new ArrayList<>());
            // if the array exists than add this to the res`s key`s value
            res.get(key).add(s);
        }

        // only returns the values as a list /return requirement 
        return new ArrayList<>(res.values());
    }
}
