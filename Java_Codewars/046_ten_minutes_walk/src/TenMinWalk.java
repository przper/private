public class TenMinWalk {
	public static boolean isValid(char[] walk) {
		if (walk.length != 10) return false;
		
		int x = 0, y = 0;
		
		for (Character c : walk) {
			if (c.equals('n')) y++;
			else if (c.equals('s')) y--;
			else if (c.equals('w')) x--;
			else x++;
		}

		return x == 0 && y==0;

	}

	public static void main(String[] args) {
		System.out.println(isValid(new char[] { 'n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's' }));
		System.out.println(isValid(new char[] { 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e' }));
		System.out.println(isValid(new char[] { 'w' }));
		System.out.println(isValid(new char[] { 'n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's' }));
		System.out.println(isValid(new char[] { 'n','w','n','w','n','w','n','w','n','w', }));

	}
}
//true, TenMinWalk.isValid(new char[] {'n','s','n','s','n','s','n','s','n','s'}));
//false, TenMinWalk.isValid(new char[] {'w','e','w','e','w','e','w','e','w','e','w','e'}));
//false, TenMinWalk.isValid(new char[] {'w'}));
//false, TenMinWalk.isValid(new char[] {'n','n','n','s','n','s','n','s','n','s'}));
