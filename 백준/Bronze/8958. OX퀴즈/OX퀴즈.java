import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		String quiz = "";
		String[] arr = new String[num];

		for (int i = 0; i < arr.length; i++) {
			quiz = sc.next();
			arr[i] = quiz;

		}
		sc.close();
	
		for (int k = 0; k < arr.length; k++) {
			int sum = 0;
			int score = 0;
			for (int m = 0; m < arr[k].length(); m++) {

				if ((arr[k].substring(m, m + 1)).equals("O")) {
					score++;
					sum = sum + score;

				} else if ((arr[k].substring(m, m + 1)).equals("X")) {
					score = 0;
					sum = sum + score;
				}

			}
			System.out.println(sum);

		}

	}
}
