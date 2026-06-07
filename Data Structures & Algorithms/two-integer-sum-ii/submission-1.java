class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int end = numbers.length -1;
        int first = 0;
        while (first<end){
            if((numbers[first]+ numbers[end]) >target)
                end -=1;
            else if(numbers[first]+ numbers[end]<target) 
                first +=1;
            else
                 return new int[]{first +1,end +1};
        }
        return new int[]{1,2};
    }
}
