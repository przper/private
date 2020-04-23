import java.util.HashMap;
import java.util.Map;

public class EightiesKids6 {

	public static String fight(Robot robot1, Robot robot2, Map<String, Integer> tactics) {
		Robot quicker, slower;
		if (robot1.getSpeed() >= robot2.getSpeed()) {
			quicker = robot1;
			slower = robot2;
		} else {
			quicker = robot2;
			slower = robot1;
		}
		int fightLength = (quicker.getTactics().length > slower.getTactics().length) ? quicker.getTactics().length
				: slower.getTactics().length;
		
		System.out.println(quicker.getTactics().length);
		System.out.println(slower.getTactics().length);
		int quickerHealth = quicker.getHealth();
		int slowerHealth = slower.getHealth();

		for (int i = 0; i < fightLength; i++) {
			System.out.println("Round: "+i);
			if (i < quicker.getTactics().length) {
				slowerHealth -= tactics.get(quicker.getTactics()[i]);
			} else {
				System.out.println("Quicker: No more attacks!");
			}
			if (slowerHealth <= 0) {
				return quicker.getName() + " has won the fight.";
			}
			
			if (i < slower.getTactics().length) {
				quickerHealth -= tactics.get(slower.getTactics()[i]);
			} else {
				System.out.println("Slower: No more attacks!");
			}
			if (quickerHealth <= 0) {
				return slower.getName() + " has won the fight.";
			}
		}

		if (quickerHealth == slowerHealth) {
			return "The fight was a draw.";
		} else if (quickerHealth > slowerHealth) {
			return quicker.getName() + " has won the fight.";
		} else {
			return slower.getName() + " has won the fight.";
		}

		// System.out.println("Slower health: " + slower.getHealth());
		// System.out.println("Quicker health: " + quicker.getHealth());
		// return "he fight was a draw."; return "he fight was a draw.";
	}

	public static void main(String[] args) {
		Robot robot1 = new Robot("Rocky", 1000, 20, new String[] { "punch", "punch", "laser", "missile" });
		Robot robot2 = new Robot("Missile Bob", 1000, 21, new String[] { "missile", "missile", "missile", "missile", "missile" });
		Map<String, Integer> tactics = new HashMap<>(3, 1f);
		tactics.put("punch", 20);
		tactics.put("laser", 30);
		tactics.put("missile", 35);
		System.out.println(EightiesKids6.fight(robot1, robot2, tactics));
		// assertEquals("Missile Bob has won the fight.", EightiesKids6.fight(robot1,
		// robot2, tactics));
	}
}
