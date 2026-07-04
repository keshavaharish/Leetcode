class Solution {
    public int removeDuplicates(int[] arr) {
        LinkedHashSet<Integer> hs=new LinkedHashSet<>();
        for(int num:arr)
        {
            hs.add(num);
        }
        int index=0;
        for(int num:hs)
        {
            arr[index++]=num;
        }
        return index;
    }
}