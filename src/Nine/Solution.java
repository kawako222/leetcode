package Nine;

import java.util.Arrays;

public class Solution {
	public int ax;
	public boolean isPalindrome(int x) {
		String l1 = String.valueOf(x);
		int[] digits = new int[l1.length()];
		int[] list2 = new int[l1.length()];
		for (int i = 0; i < l1.length(); i++) {
			digits[i] = l1.charAt(i) - '0'; 
			list2[i] = l1.charAt(l1.length()-i-1) - '0';
		}
		
		if(Arrays.equals(digits, list2)) {
			
			System.out.println("True");
			return true;
		}
		else {
			System.out.println("False");
			return false;
		}
		
	}
	
	
	public static void main(String[] args) {
		Solution Obj1 = new Solution();
		boolean a = Obj1.isPalindrome(10);
		if (a == true) {
			System.out.println("Is palindrome");
		}
	}
}
