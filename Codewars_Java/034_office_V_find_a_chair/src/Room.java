
public class Room {
	public String occupants; // number of occupants, each occupant is represented by 'X'
	public int chairs; // number of chairs in the room

	public Room(String occupants, int chairs) {
		super();
		this.occupants = occupants;
		this.chairs = chairs;
	}

	public String getOccupants() {
		return occupants;
	}

	public void setOccupants(String occupants) {
		this.occupants = occupants;
	}

	public int getChairs() {
		return chairs;
	}

	public void setChairs(int chairs) {
		this.chairs = chairs;
	}

}
