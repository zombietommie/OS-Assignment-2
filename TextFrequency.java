/*
 * Tommy Tran 2420005
 *
 * CSCI 4401 OS
 *
 * Assigment 2:
 * Exercise 1 - No threads
 *
 */ 

// imports
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class TextFrequency {
    public static void main(String [] args) {
        try {
            File textFile = new File("enwik9");
            Scanner reader = new Scanner(textFile);
            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                System.out.println(data);
            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error has occurred!");
            e.printStackTrace();
        }
    }
}
