class Solution {
    public int longestConsecutive(int[] nums) {
        
        // using hash map

        Map<Integer , Integer> map = new HashMap<>();

        int longest = 0;

        for(int n : nums){
            if(!map.containsKey(n)){

                // num - 1 (left neighbor)
                // num + 1 (right neighbor)
                map.put(n, map.getOrDefault(n - 1, 0) + map.getOrDefault(n + 1, 0) + 1);


                map.put(n - map.getOrDefault(n-1,0), map.get(n));
                map.put(n+map.getOrDefault(n+1,0), map.get(n));
                longest = Math.max(longest, map.get(n));
            }
        }
        
        return longest;
        
    // useing hash set
    //     Set<Integer> numSet = new HashSet<>();
    //     for (int n: nums){
    //         numSet.add(n);
    //     }
    //     int longest = 0;
    //     for(int n: numSet){
    //         if(!numSet.contains(n-1)) {
    //             int length = 0;
    //             while(numSet.contains(n + length)){
    //                 length++;
    //             }
    //             longest = Math.max(longest , length);
    //         }
    //     }
    //     return longest;
    // }
}
}