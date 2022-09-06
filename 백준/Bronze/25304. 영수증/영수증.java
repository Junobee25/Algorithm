import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int total = sc.nextInt();
		int number = sc.nextInt();
		int sum = 0;
		for (int i = 0; i < number; i++) {
			int price = sc.nextInt();
			int it_num = sc.nextInt();
			sum += (price * it_num);

		}

		if (sum == total) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}

	}
}
