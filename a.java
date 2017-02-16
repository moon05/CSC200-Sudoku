//takes two parameters 
//first parameter is the size of the board (sudoku is 9)
//second parameter is the number of initial variables

public class a{
	
	public static void sudoku( int n, int initVar){
		int[][] board = new int[n][n];
		
		//initializing the variables to 0
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				board[i][j] = 0;
			}
		}
		
		//filling in initVar
		int col, row, cellValue;
		col = (int)(Math.random()*9);
		row = (int)(Math.random()*9);
		cellValue = 1 + (int)(Math.random()*9);
		
		//this loop will go initVar times
		for( int i=0; i<initVar; i++){	
			//now pick a random(1-9) for col and row and cellValue
			col = (int)(Math.random()*9);
			row = (int)(Math.random()*9);
			cellValue = 1 + (int)(Math.random()*9);
			while (board[row][col]==0){
				col = (int)(Math.random()*9);
				row = (int)(Math.random()*9);
				cellValue = 1 + (int)(Math.random()*9);
			}
				
		}
		
		
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				System.out.print("\t"+board[i][j] );
			}
			System.out.println();
		}
		
	}
	
	public static void main(String a[]){
		int size = 9;
		size = Integer.parseInt(a[0]);
		int initVar = 2;
		initVar = Integer.parseInt(a[1]);
		
		sudoku(size, initVar);
	}
}
