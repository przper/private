public class Kata {
    public static String declareWinner(Fighter fighter1, Fighter fighter2, String firstAttacker) {
        while (fighter1.health>0 || fighter2.health>0) {
            if (fighter1.name.equals(firstAttacker)) {
                fighter2.health-=fighter1.damagePerAttack;
                System.out.println(fighter2.name+" has "+fighter2.health+" HP remaining");
                if (fighter2.health<=0) {
                    return fighter1.name;
                }

                fighter1.health-=fighter2.damagePerAttack;
                System.out.println(fighter1.name+" has "+fighter1.health+" HP remaining");
                if (fighter1.health<=0) {
                    return fighter2.name;
                }

            } else {
                fighter1.health-=fighter2.damagePerAttack;
                System.out.println(fighter1.name+" has "+fighter1.health+" HP remaining");
                if (fighter1.health<=0) {
                    return fighter2.name;
                }

                fighter2.health-=fighter1.damagePerAttack;                
                System.out.println(fighter2.name+" has "+fighter2.health+" HP remaining");
                if (fighter2.health<=0) {
                    return fighter1.name;
                }
            }
        }

        return null;}

    public static void main(String args[]) {
        Fighter Lew = new Fighter("Lew", 10, 2);
        Fighter Harry = new Fighter("Harry", 5, 4);
        Fighter Jerry = new Fighter("Jerry", 30, 3);
        Fighter Harald = new Fighter("Harald", 20, 5);

        System.out.println(declareWinner(Lew,Harry,"Lew")+" wins!");

    }
}