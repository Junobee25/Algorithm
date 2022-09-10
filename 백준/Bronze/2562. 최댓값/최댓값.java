import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int input[] = new int[9];
        int max=0;
        int max_index = 0;


        for (int i =0;i<input.length;i++) {
            input[i]=in.nextInt();
        }

        for (int i =0;i<input.length;i++) {
            if(input[i]>max) {
                max = input[i];
                max_index=i;
            }
        }

        System.out.println(max);
        System.out.println(max_index+1);


    }
}
