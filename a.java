//takes two parameters 
//first parameter is the size of the board (sudoku is 9)
//second parameter is the number of initial variables
//outputs in cnf
//newline at end of file

public class a{
	
	public static int CNFmultiplier = 10;
	
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
		col = (int)(Math.random()*n);
		row = (int)(Math.random()*n);
		cellValue = 1 + (int)(Math.random()*n);
		
		//this loop will go initVar times
		for( int i=0; i<initVar; i++){	
			//now pick a random(1-9) for col and row and cellValue
			col = (int)(Math.random()*n);
			row = (int)(Math.random()*n);
			cellValue = 1 + (int)(Math.random()*n);
			//if cell is already filled, repeat iteration
			if(board[row][col]!=0){
				i--;
				continue;
			}
			board[row][col] = cellValue;				
		}		
		
		//array to store the output in cnf
		int[] output = new int[initVar];
		int count = 0;
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				//uncomment the next line to print grid
				//System.out.print("\t"+board[i][j] );
				if(board[i][j]!=0) {
					output[count++] = ((i+1)*CNFmultiplier*CNFmultiplier) + ((j+1)*CNFmultiplier) + board[i][j];
				}
			}
			//uncomment the next line to prnt grid
			//System.out.println();
		}
		
		//printing the output loop
		for(int i=0; i<initVar; i++) {
			System.out.print(output[i]+"\n");
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
