
import java.util.Arrays;

public class Travel {

    public static String travel(String r, String zipcode) {
        String[] result = {zipcode, "", ""};

        for (String a : r.split(",")) {
            String number = a.split(" ")[0];

            String street = "";
            for (int i = 1; i < a.split(" ").length - 2; i++) {
                if (street != "") {
                    street += " ";
                }
                street += a.split(" ")[i];
            }

            String postalCode = a.split(" ")[a.split(" ").length - 2] + " " + a.split(" ")[a.split(" ").length - 1];

            if (postalCode.equals(zipcode)) {

                if (result[1] != "") {
                    result[1] += ",";
                }
                result[1] += street;

                if (result[2] != "") {
                    result[2] += ",";
                }
                result[2] += number;

            }
        }
        
        return result[0] + ":" + result[1] + "/" + result[2];
    }

    public static void main(String args[]) {
        String ad = "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
                + "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
                + "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
                + "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
                + "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
                + "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
                + "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
                + "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
                + "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
                + "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
                + "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
                + "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000";

        String code = "OH 43071,NY 56432,ZP 32908,AE 56210,RE 13000,EX 34342,SW 43098,AA 45521,GG 30654,ZP 32908,AE 56215,RE 13200,EX 34345,"
                + "RE 13222,RE 13001,SW 43198,AA 45522,GG 30655,XX 32321,YY 45098";

        System.out.println(travel(ad, "XX 32321"));
    }
}
