class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq =  new HashMap<>();
        // here get the frequency of elemets in array nums
        for(int i : nums){
            freq.put(i , freq.getOrDefault(i,0)+1);
        }

        // ex:nums=[1,1,2,2,2,3],k=2
        // freq = [[1:2],[2:3],[3:1]]={value:frequency}

        List<int[]>arr = new ArrayList<>();
        // here entrySet() has values like get(i).[0] = value or key
        for(Map.Entry<Integer, Integer>entry: freq.entrySet()){
            // here arr will be setted with frequency:value 

            // bcz freq was in value:frequency . Now arr will be frequency:value
            arr.add(new int[]{entry.getValue(),entry.getKey()});
        }
            // soring the arr with using [0] means according to the frequency of array
            arr.sort((a,b)->b[0]-a[0]);

            int[] res = new int[k];
            for(int i=0;i<k;i++){
                // getting the top k = 2 values with highes frequency. here [1]= the elemnt of nums
                res[i]= arr.get(i)[1];
            }
        return res;

        }

    }
    

