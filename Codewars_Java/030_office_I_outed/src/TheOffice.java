class Person {
	String name; // team memnber's name
	int happiness; // happiness rating out of 10

	public Person(String name, int happiness) {
		super();
		this.name = name;
		this.happiness = happiness;
	}

}

public class TheOffice {
	public static String outed(Person[] meet, String boss) {
		double happiness = 0;
		for (Person p : meet) {
			if (p.name.equals(boss)) {
				happiness += 2 * p.happiness;
			} else {
				happiness += p.happiness;
			}
		}
		happiness = happiness / meet.length;
		
		if (happiness > 5) {
			return "Nice Work Champ!";
		} else {
			return "Get Out Now!";
		}
	}

	public static void main(String[] args) {
		Person[] meet = new Person[] { new Person("tim", 0), new Person("jim", 2), new Person("randy", 0),
				new Person("sandy", 7), new Person("andy", 0), new Person("katie", 5), new Person("laura", 1),
				new Person("saajid", 2), new Person("alex", 3), new Person("john", 2), new Person("mr", 0) };

		System.out.println(outed(meet, "laura"));
	}
}