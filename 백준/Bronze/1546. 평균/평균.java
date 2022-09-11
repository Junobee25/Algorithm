import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		double[] arr = new double[num1];

		int num = 0;
		double imax = -99999;
		double sum = 0;

		for (int i = 0; i < arr.length; i++) {
			num = sc.nextInt();
			arr[i] = num;
		}
		for (int j = 0; j < arr.length; j++) {
			imax = Math.max(arr[j], imax);

		}
		for (int k = 0; k < arr.length; k++) {
			if (arr[k] <= imax) {
				arr[k] = arr[k] / imax * 100;
			}
		}
		for (int m = 0; m < arr.length; m++) {
			sum += arr[m];

		}
		System.out.println(sum / arr.length);
	}

}