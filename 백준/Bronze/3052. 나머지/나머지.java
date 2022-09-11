import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[10];
		int[] re = new int[10];
		int cnt = 1;

		int num = 0;
		for (int i = 0; i < arr.length; i++) {
			num = sc.nextInt();
			arr[i] = num;
			re[i] = arr[i] % 42;
		}

		Arrays.sort(re);
		for (int k = 0; k < re.length - 1; k++) {
			if (re[k] == re[k + 1]) {

			} else if (re[k] != re[k + 1]) {
				cnt++;

			}

		}
		System.out.println(cnt);

	}

}