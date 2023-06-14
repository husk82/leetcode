import java.util.*;

public class searchMatrix74 {
	
	public boolean searchMatrix(int[][] matrix, int target) {
		
		int row = matrix.length;
		int col = matrix[0].length;
		
		int l = 0;
		int r = row * col - 1;
		
		while (l <= r) {
			
			int midpoint = (l + r) / 2;
			int c1 = midpoint % col;
			int r1 = (midpoint - c1) / col; 
			
			if (matrix[r1][c1] == target) return true;
			else if (target > matrix[r1][c1]) l = midpoint + 1;
			else if (target < matrix[r1][c1]) r = midpoint - 1;
		}
		return false;
	}
	
}
