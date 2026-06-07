class Solution {
    public int[] twoSum(int[] nums, int target) {

    Map<Integer,Integer> ele=new HashMap<>();
    for(int i=0;i<nums.length;i++){
        ele.put(nums[i],i);
    }

    for(int i=0;i<nums.length;i++){
        int el2=target - nums[i];
        // without same value indeces check got wa
        if(ele.containsKey(el2)&&ele.get(el2)!=i){
            return new int[]{i,ele.get(el2)};
        }
    }
// brute force
// for(int i=0;i<nums.length;i++){
//     int b = target-nums[i];
//     for(int j=i+1;j<nums.length;j++){
//         if(b==nums[j]){
//             return new int[]{i,j};
//         }
//     }

// }  
 return new int[] {1,0};      
        
    }
}
