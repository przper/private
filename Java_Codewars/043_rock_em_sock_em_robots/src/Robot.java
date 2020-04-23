import java.util.Arrays;

public class Robot {
	String name;
	int health;
	int speed;
	String[] tactics;

	public Robot(String name, int health, int speed, String[] tactics) {
		super();
		this.name = name;
		this.health = health;
		this.speed = speed;
		this.tactics = tactics;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getHealth() {
		return health;
	}

	public void setHealth(int health) {
		this.health = health;
	}

	public int getSpeed() {
		return speed;
	}

	public void setSpeed(int speed) {
		this.speed = speed;
	}

	public String[] getTactics() {
		return tactics;
	}

	public void setTactics(String[] tactics) {
		this.tactics = tactics;
	}

	@Override
	public String toString() {
		return "Robot [name=" + name + ", health=" + health + ", speed=" + speed + ", tactics="
				+ Arrays.toString(tactics) + "]";
	}

}
