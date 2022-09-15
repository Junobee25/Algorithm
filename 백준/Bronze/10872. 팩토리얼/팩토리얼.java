import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int pack = 1;

		for (int i = num; i >= 1; i--) {

			pack *= i;

		}
		System.out.println(pack);

	}

}
