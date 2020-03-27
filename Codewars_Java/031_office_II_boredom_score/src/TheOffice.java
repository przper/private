import java.util.HashMap;
import java.util.Map;

public class TheOffice {

	public static String boredom(Person[] staff) {
		Map<String, Integer> map = new HashMap<>();
		map.put("accounts", 1);
		map.put("finance", 2);
		map.put("canteen", 10);
		map.put("regulation", 3);
		map.put("trading", 6);
		map.put("change", 6);
		map.put("IS", 8);
		map.put("retail", 5);
		map.put("cleaning", 4);
		map.put("pissing about", 25);
		int happinessLevel = 0;
		for (Person p : staff) {
			happinessLevel += map.get(p.department);
		}

		System.out.println(happinessLevel);
		
		if (happinessLevel > 80 ) {
			return "party time!!";
		} else if (80 < happinessLevel && happinessLevel < 100 ){
			return "i can handle this";
		} else {
			return "kill me now";
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person[] team = { new Person("tim", "change"), new Person("jim", "accounts"), new Person("randy", "canteen"),
				new Person("sandy", "change"), new Person("andy", "change"), new Person("katie", "IS"),
				new Person("laura", "change"), new Person("saajid", "IS"), new Person("alex", "trading"),
				new Person("john", "accounts"), new Person("mr", "finance") };

		System.out.println(boredom(team));
	}

}
