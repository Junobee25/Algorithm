import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int ar[] = new int[10];
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();

		int num = a * b * c;
		while(num>0) {
			ar[num%10]++;
			num /= 10;
			
		}
		for(int i =0; i<10;i++) {
			System.out.println(ar[i]);
		}
		
	}

}