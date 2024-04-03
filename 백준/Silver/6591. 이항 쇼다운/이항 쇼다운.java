import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        solve(sc);
    }

    public static void solve(Scanner sc) {
        StringBuilder sb = new StringBuilder();
        while (true) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int div = 1;
            long ans = 1;
            if (a == 0 && b == 0) {
                break;
            }
            if (a - b < b) {
                b = a - b;
            }
            while (b-- > 0) {
                ans *= a--;
                ans /= div++;
            }
            sb.append(ans + "\n");
        }
        System.out.println(sb.toString());
    }
}