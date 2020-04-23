import java.util.HashMap;
import java.util.Map;

public class BattleShips {

	public static Map<String, Double> damagedOrSunk(final int[][] board, final int[][] attacks) {
		Map<String, Double> result = new HashMap<String, Double>();
		result.put("sunk", 0.0);
		result.put("damaged", 0.0);
		result.put("notTouched", 0.0);
		result.put("points", 0.0);

		// create a map with ships and their size
		Map<Integer, Integer> shipSizeMap = new HashMap<>();
		// create a map with ships and their health
		Map<Integer, Integer> shipHealthMap = new HashMap<>();
		for (int[] row : board) {
			for (int i : row) {
				if (i != 0) {
					shipSizeMap.put(i, shipSizeMap.getOrDefault(i, 0) + 1);
					shipHealthMap.put(i, shipHealthMap.getOrDefault(i, 0) + 1);
				}
			}
		}

		// attackBoardSetter
		int sizeX = board[0].length;
		int sizeY = board.length;
		int[][] attackBoard = new int[sizeY][sizeX];
		for (int[] attack : attacks) {
			int x = attack[0] - 1;
			int y = sizeY - attack[1]; // invertion
			attackBoard[y][x] = 1;
		}

		// travel through boards and reduce ship health
		for (int y = 0; y < sizeY; y++) {
			for (int x = 0; x < sizeX; x++) {
				if (board[y][x] != 0 && attackBoard[y][x] != 0) {
					shipHealthMap.put(board[y][x], shipHealthMap.getOrDefault(board[y][x], 0) - 1);
				}
			}
		}

		printBoard(board);
		for (int i : shipSizeMap.keySet()) {
			System.out.println("Ship index: " + i + " Ship size: " + shipSizeMap.get(i));
		}
		System.out.println("-----------");

		printBoard(attackBoard);
		System.out.println("-----------");
		for (int i : shipHealthMap.keySet()) {
			System.out.println("Ship index: " + i + " Ship health: " + shipHealthMap.get(i));
		}

		//System.out.println(result.get("damaged"));
		
		// count score
		for (int i : shipHealthMap.keySet()) {
			// sunken boats
			if (shipHealthMap.get(i) == 0) {
				double num = result.get("sunk")+1;
				//System.out.println(num);
				result.replace("sunk", num);
				System.out.println(i+" 1 "+result.get("sunk"));
			}
			// damaged
			if (shipHealthMap.get(i) < shipSizeMap.get(i) && shipHealthMap.get(i) > 0) {
				double num = result.get("damaged")+1;
				result.replace("damaged", num);
				System.out.println(i+" 2 "+result.get("damaged"));
			}
			// nottouched
			if (shipHealthMap.get(i) == shipSizeMap.get(i)) {
				double num = result.get("notTouched")+1;
				result.replace("notTouched", num);
				System.out.println(i+" 3 "+result.get("notTouched"));
			}
		}

		double points = 0;
		points += result.get("sunk")*1;
		points += result.get("damaged")*0.5;
		points += result.get("notTouched")*(-1);
		System.out.println("Points: "+points);
		result.replace("points", points);
		
		
		return result;
	}

	public static void printBoard(int[][] board) {
		int sizeX = board[0].length;
		int sizeY = board.length;
		for (int y = 0; y < sizeY; y++) {
			StringBuilder sb = new StringBuilder();
			for (int x = 0; x < sizeX; x++) {
				sb.append(board[y][x]);
			}
			System.out.println(sb.toString());
		}
	}

	public static void main(String[] args) {

		int[][] board = new int[][] { new int[] { 3, 0, 1 }, new int[] { 3, 0, 1 }, new int[] { 0, 2, 1 },
				new int[] { 0, 2, 0 } };
		int[][] attacks = new int[][] { new int[] { 2, 1 }, new int[] { 2, 2 }, new int[] { 3, 2 },
				new int[] { 3, 3 } };

		Map<String, Double> expected = new HashMap<String, Double>();
		expected.put("sunk", 1.0);
		expected.put("damaged", 1.0);
		expected.put("notTouched", 1.0);
		expected.put("points", 0.5);

		damagedOrSunk(board, attacks);

	}

}
