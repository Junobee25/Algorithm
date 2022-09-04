import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();

		for (int i = 1; i <= num1; i++) {
			int num2 = sc.nextInt();
			int num3 = sc.nextInt();
			System.out.println(num2 + num3);
		}

	}

}