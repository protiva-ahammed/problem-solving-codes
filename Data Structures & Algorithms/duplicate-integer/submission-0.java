class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer>has=new HashSet<>();
        for(int i=0;i<nums.length;i++){
            boolean a = has.add(nums[i]);
            if(!a) return true;

        }
        return false;
        
    }
}