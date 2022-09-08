import java.util.Scanner;
import java.util.ArrayList;
public class Main {

	public static void main(String[] args) { 
			Scanner sc=new Scanner(System.in);
			int num=sc.nextInt();
			ArrayList<Integer> list=new ArrayList();
			int a, b;
			
			for(int i=0; i<num;i++) {
				a=sc.nextInt();
				b=sc.nextInt();
				list.add(a);
				list.add(b);
			}
			for(int i=0;i<num;i++) {
				int case_num=i+1;
				int A=list.get(2*i);
				int B=list.get(2*i+1);
				System.out.println("Case #"+case_num+": "+A+" + "+B+" = "+(A+B));
			}
	


	
	}

}