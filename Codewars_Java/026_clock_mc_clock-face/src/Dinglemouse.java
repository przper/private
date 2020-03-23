import java.time.LocalTime;

public class Dinglemouse {

	public static String whatTimeIsIt(final double angle) {
		if (angle < 30) {
			int minutes = (int) (angle / 0.5);
			return LocalTime.of(12, minutes).toString();
		}

		int allMinutes = (int) (angle / 0.5);
		int hours = allMinutes / 60;
		int minutes = allMinutes - 60 * hours;

		LocalTime lt = LocalTime.of(hours, minutes);

		return lt.toString();
	}

}