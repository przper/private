import java.util.LinkedList;
import java.util.List;

public class TheOffice {

	public static Object meeting(Room[] x, int need) {
		if (need == 0) {
			return "Game On";
		}

		List<Integer> result = new LinkedList<>();
		int available = 0;
		int i = 0;

		while (available < need && i < x.length) {
			int chairs = x[i].chairs - x[i].occupants.length();
			if (chairs >= 0) {
				result.add(chairs);
			} else {
				result.add(0);
			}
			available += result.get(i);
			i++;
		}
		if (available == need) {
			return result.toArray();
		} else {
			return "Not enough!";
		}
	}

	public static void main(String[] args) {
		Room[] rooms = new Room[] { new Room("XXX", 3), new Room("XXXXX", 6), new Room("XXXXXX", 9) };
		System.out.println(meeting(rooms, 4));
		System.out.println(meeting(rooms, 4).equals(new int[] { 0, 1, 3 }));
	}

}
