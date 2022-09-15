import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int cnt = sc.nextInt();

		int val1 = 0;
		

		for (int i = 0; i < cnt; i++) {
			int num = sc.nextInt();
			for (int j = 2; j <= num; j++) {
				if ( j == num) {
					val1++;
				}

				if (num % j == 0) {
					break;

				} 
				

			}
			

		}
		System.out.println(val1);

	}
}
