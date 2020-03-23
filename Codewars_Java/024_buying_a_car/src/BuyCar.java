public class BuyCar {

	public static int[] nbMonths(int startPriceOld, int startPriceNew, int savingPerMonth, double percentLossByMonth) {
		double savings = 0;
		int counter = 0;
		double updatedPriceNew = startPriceNew;
		double updatedPriceOld = startPriceOld;
		double percentLoss = percentLossByMonth;
		double available = -updatedPriceNew + savings + updatedPriceOld;
		while (available < 0) {
			// System.out.println(available < 0);
			// System.out.println("available" + available);
			// System.out.println("updatedPriceNew" + updatedPriceNew);
			savings += savingPerMonth;
			counter += 1;
			if (counter % 2 == 0) {
				percentLoss += 0.5;
			}
			updatedPriceNew = updatedPriceNew * (1 - percentLoss * 0.01);
			updatedPriceOld = updatedPriceOld * (1 - percentLoss * 0.01);
			available = -updatedPriceNew + savings + updatedPriceOld;
			System.out.println("end month " + counter + ": percentLoss " + percentLoss + " available " + available);

		}
		int[] result = { counter, (int) Math.round(available) };
		return result;
	}

	public static void main(String[] args) {
		System.out.println(nbMonths(2000, 8000, 1000, 1.5));
	}
}