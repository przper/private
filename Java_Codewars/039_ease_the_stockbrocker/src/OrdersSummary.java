import java.util.LinkedList;
import java.util.List;

public class OrdersSummary {

	public static String balanceStatements(String lst) {
		// Quote[0]/white-space/Quantity[1]/white-space/Price[2]/white-space/Status[3]
		int toBuySum = 0;
		int toSellSum = 0;
		List<String> strBadOrders = new LinkedList<>();
		String correctOrderRegex = "\\S+ \\d+ \\d*\\.\\d* [BS]";
		
		for (String order : lst.split(", ?")) {
			String[] details = order.split(" ");
			if (!order.matches(correctOrderRegex)) {
				strBadOrders.add(order);
			} else {
				if (details[3].equals("B")) {
					toBuySum += Math.round(Double.parseDouble(details[1]) * Double.parseDouble(details[2]));
				} else {
					toSellSum += Math.round(Double.parseDouble(details[1]) * Double.parseDouble(details[2]));
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		sb.append("Buy: "+toBuySum+" Sell: "+toSellSum);
		if (strBadOrders.size()>0 && lst.length()>0) {
			sb.append("; Badly formed "+strBadOrders.size()+": ");
			for (int i=0; i<strBadOrders.size();i++ ) {
				sb.append(""+strBadOrders.get(i)+" ;");
			}
		}
		return sb.toString();
	}

	public static void main(String[] args) {
		String l = "ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B";
		System.out.println(balanceStatements(l));
	}
}

//String l = "ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B";	
//assertEquals("Buy: 29499 Sell: 0", OrdersSummary.balanceStatements(l));
