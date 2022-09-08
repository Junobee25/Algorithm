import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int ans = sc.nextInt();
		int cnt = 1;
		while (true) {
			if(num<cnt) {
				break;
			}
			int num1 = sc.nextInt();
			if (num1 < ans) {
				System.out.print(num1 + " ");
			}

			cnt++;

		}

	}

}
