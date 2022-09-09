import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String num1 = sc.next();
		int num3 = 0;
		int cnt = 0;
		String c = "";
		int num2 = Integer.parseInt(num1);

		if (num2 < 10) {
			num1 = "0" + num1;

		}
		String ans = num1;
		while (true) {
			
			String i = num1.substring(0, 1);
			String j = num1.substring(1, 2);

			int k = Integer.parseInt(i);
			int m = Integer.parseInt(j);
			num3 = k + m;

			String a = Integer.toString(m);
			String b = Integer.toString(num3);
			if (b.length() >= 2) {
				b = b.substring(1, 2);

			}
			c = a + b;
			
			cnt++;
			if (ans.equals(c)) {
				break;
			}
			num1 = c;
			
			

		}

		System.out.println(cnt);
	}

}
