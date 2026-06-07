class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> res = new HashMap<>();
        for(int i: nums){
            res.put(i,res.getOrDefault(i,0)+1);
        }

        // exchanging values
        List<int[]> arr = new ArrayList<>();

        for(Map.Entry<Integer,Integer>entry: res.entrySet()){
            arr.add(new int[]{entry.getValue(),entry.getKey()});
        }
        arr.sort((a,b)->b[0]-a[0]);
int ans[] = new int[k];
for(int i=0;i<k;i++){
    ans[i]=arr.get(i)[1];
}

        return ans;
  
    }

}
