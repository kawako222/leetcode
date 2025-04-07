package One;
import java.util.Scanner;


public class Solution {
	 int[] arr = new int[5];
	 int[] two = new int[2];
	 public int n;
	 public int target;
	 
	 public int getN() {
			return n;
		}
	 public int getTarget() {
			return n;
		}
	 public void setN(int n) {
			this.n = n;
		}
	 public void setTarget(int target) {
			this.target = target;
		}
	 
	 public void enterNum() {
		 Scanner in = new Scanner(System.in);
		 System.out.print("Enter the lenght of number in the array; ");
		 setN(in.nextInt()); 
		 
		 for(int i=0;i<n;i++) {
			 System.out.print("Enter " +  i + ": ");
			 arr[i] = in.nextInt();
		 }
		 System.out.print("Enter the targeted number; ");
		 setTarget(in.nextInt()); 
	 }
	 
	 public void getNewArray() {
			 for(int i=0;i<n;i++) {
				 for(int j=i+1;j<n;j++) {			
					 if(arr[i] + arr[j] == target) {
						 two[0] = arr[i];
						 two[1] = arr[j];
						 return;					 
					 }
				 }
			 }
		 
	 }
	 public void printArr() {
		 for(int i=0;i<2;i++) {
			 System.out.println("Number: " +  two[i]);
		 }
	 }
	 
}
