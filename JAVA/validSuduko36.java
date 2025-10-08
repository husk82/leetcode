import java.util.*;

public class validSuduko36 {

	public boolean isValidSudoku(char[][] board) {
			
		Map<Integer, Set<Character>> row = new HashMap<>();
		Map<Integer, Set<Character>> col = new HashMap<>();
		Map<Integer, Set<Character>> box = new HashMap<>();
		
		for (int i=0; i<9; i++) {
			for (int j=0; j<9; j++) {
				
				int boxIndex = (int) (i/3) * 3 + (j/3);
				
				if (board[i][j] == '.') {
					continue;
				}
				if (row.getOrDefault(i, new HashSet<>()).contains(board[i][j]) || 
						col.getOrDefault(j, new HashSet<>()).contains(board[i][j]) || 
						box.getOrDefault(boxIndex, new HashSet<>()).contains(board[i][j])) {
					return false;
				}
				
				
				Set<Character> rowSet = row.getOrDefault(i, new HashSet<>());
				rowSet.add(board[i][j]);
				row.put(i, rowSet);
				
				Set<Character> colSet = col.getOrDefault(j, new HashSet<>());
				colSet.add(board[i][j]);
				col.put(j, colSet);
				
				Set<Character> boxSet = box.getOrDefault(boxIndex, new HashSet<>());
				boxSet.add(board[i][j]);
				box.put(boxIndex, boxSet);	
			}
		}
		return true;
    }
	
}
