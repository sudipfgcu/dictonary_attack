import java.io.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.xml.bind.DatatypeConverter;
import java.util.Scanner;

public class DictionaryAttackJava {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your password: ");
        String password = scanner.nextLine();
        savePassword(password);
        dictionaryAttack();
        scanner.close();
    }

    private static void savePassword(String password) {
        try {
            String hashedPassword = stringToSha1(password);
            try (PrintWriter out = new PrintWriter("password.txt")) {
                out.println(hashedPassword);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void dictionaryAttack() {
        try {
            String hashedPassword = new BufferedReader(new FileReader("password.txt")).readLine();
            BufferedReader dictionary = new BufferedReader(new FileReader("english.0"));
            String line;
            int attempts = 0;
            long startTime = System.currentTimeMillis();
            boolean found = false;

            while ((line = dictionary.readLine()) != null && !found) {
                attempts++;
                if (hashedPassword.equals(stringToSha1(line.trim()))) {
                    long elapsed = System.currentTimeMillis() - startTime;
                    try (PrintWriter out = new PrintWriter("crackedpassword.txt")) {
                        out.println("The password is: " + line.trim());
                        out.println("Attempts: " + attempts);
                        out.println("Time taken: " + elapsed / 1000.0 + " seconds");
                    }
                    System.out.println("Password cracked: " + line.trim());
                    System.out.println("Attempts: " + attempts);
                    System.out.println("Time taken: " + elapsed / 1000.0 + " seconds");
                    found = true;
                }
            }

            if (!found) {
                long elapsed = System.currentTimeMillis() - startTime;
                try (PrintWriter out = new PrintWriter("crackedpassword.txt")) {
                    out.println("Password could not be cracked.");
                    out.println("Attempts: " + attempts);
                    out.println("Time taken: " + elapsed / 1000.0 + " seconds");
                }
                System.out.println("Password could not be cracked.");
                System.out.println("Attempts: " + attempts);
                System.out.println("Time taken: " + elapsed / 1000.0 + " seconds");
            }

            dictionary.close();
        } catch (IOException | NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }

    private static String stringToSha1(String input) throws NoSuchAlgorithmException, UnsupportedEncodingException {
        MessageDigest sha1 = MessageDigest.getInstance("SHA1");
        byte[] inputBytes = input.getBytes("UTF-8");
        byte[] hashBytes = sha1.digest(inputBytes);
        return DatatypeConverter.printHexBinary(hashBytes);
    }
}
