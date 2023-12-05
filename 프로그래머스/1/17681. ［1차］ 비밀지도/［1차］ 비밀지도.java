import java.util.Arrays;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        
        String[] decodeArr1 = decodeBinaryNumber(n, arr1);
        String[] decodeArr2 = decodeBinaryNumber(n, arr2);
        
        return concatDecodeArr(decodeArr1, decodeArr2);
    };
    
    public String[] decodeBinaryNumber(int n, int[] arr) {
        String[] decodeArr = new String[n];
        
        for (int idx = 0; idx < arr.length; idx++) {
            decodeArr[idx] = dataPreprocessing(n,binaryNumberToSharpOrGap(arr[idx]));
        }
        
        return decodeArr;
    };
    
    public String binaryNumberToSharpOrGap(int element) {
        int value = element;
        String result = "";
        
        while (value >= 1) {
            int mod = value % 2;
            value = value / 2;
            result += modToSharpOrGap(mod);
        };
        
        return result;
    };
    
    public String modToSharpOrGap(int mod) {
        if (mod == 1) {
                return "#";
            };
        
        return " ";
    };
    public String dataPreprocessing(int n, String data) {
        int diff = n - data.length();
        if (diff > 0) {
            String newData = data + " ".repeat(diff);
            StringBuffer sb = new StringBuffer(newData);        
            String result = sb.reverse().toString();
            return result;
        }
        
        StringBuffer sb = new StringBuffer(data);
        String result = sb.reverse().toString();
        return result;
    }
    
    public String[] concatDecodeArr(String[] arr1, String[] arr2) {
        String[] result = new String[arr1.length];
        
        for(int i = 0; i < arr1.length; i++) {
            String element = "";
            for (int j = 0; j < arr1.length; j++) {
                if (arr1[i].charAt(j) == ' ' && arr2[i].charAt(j) == ' ') {
                    element += " ";
                }
                if (arr1[i].charAt(j) == '#' || arr2[i].charAt(j) == '#') {
                    element += "#";
                }
            }
            result[i] = element;
        }
        return result;
    }
}