/*
 * Tommy Tran 2420005
 *
 * CSCI 4401 OS
 *
 * Assigment 2:
 * Exercise 1 - With threads
 * 
 */

// imports
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


class TextFrequencyThreaded implements Runnable {
    public static void main(String[] args) {
        TextFrequencyThreaded obj = new TextFrequencyThreaded();
        Thread thObj = new Thread(obj);
        thObj.start();
    }

    private String newData;
    private float totalCount = 0;
    private float[] counts = new float[8];
    private long startTime = System.nanoTime();

    public void run() {

        // try catch to make sure the file is going to be found and read and printed
        try {
            // Using the File, grab the source text
            File textFile = new File("enwik9");
            // Use the Scanner to read the 'textFile'
            Scanner reader = new Scanner(textFile);
            // loop through each line and read each line
            while (reader.hasNextLine()) {
                // read the line
                String data = reader.nextLine();
                // remove symbols
                newData = data.replaceAll("[^a-zA-Z0-9_-]", " ");
                String[] splitWord = newData.split("\\s+");
                for (int i = 0; i < splitWord.length; i++) {
                    String theWord = splitWord[i];
                    if (theWord.length() == 1) {
                        counts[0] += 1;
                    } else if (theWord.length() == 2) {
                        counts[1] += 1;
                    } else if (theWord.length() == 3) {
                        counts[2] += 1;
                    } else if (theWord.length() == 4) {
                        counts[3] += 1;
                    } else if (theWord.length() == 5) {
                        counts[4] += 1;
                    } else if (theWord.length() == 6) {
                        counts[5] += 1;
                    } else if (theWord.length() == 7) {
                        counts[6] += 1;
                    } else if (theWord.length() >= 8) {
                        counts[7] += 1;
                    } else {
                        // Do nothing
                    }
                }
            }
            // File closer Required
            reader.close();
            // catch an error if the file is not found
        } catch (FileNotFoundException e) {
            System.out.println("An error has occurred!");
            e.printStackTrace();
        }

        // add and get total words in file
        int j = 0;
        while (j < counts.length) {
            totalCount += counts[j];
            j++;
        }

        System.out.printf(
                "1 letter word: %.0f - %.01f%%\n2 letter words: %.0f - %.01f%%\n3 letter words: %.0f - %.01f%%\n4 letter words: %.0f - %.01f%%\n5 letter words: %.0f - %.01f%%\n6 letter words: %.0f - %.01f%%\n7 letter words: %.0f - %.01f%%\n8 or more letter words: %.0f - %.01f%%\n",
                counts[0], percentWord(counts[0], totalCount), counts[1], percentWord(counts[1], totalCount), counts[2],
                percentWord(counts[2], totalCount), counts[3], percentWord(counts[3], totalCount), counts[4],
                percentWord(counts[4], totalCount), counts[5], percentWord(counts[5], totalCount), counts[6],
                percentWord(counts[6], totalCount), counts[7], percentWord(counts[7], totalCount));

        long endTime = System.nanoTime();
        System.out.println((endTime - startTime) / 1000000000 + " seconds runtime.");
    }

    public static float percentWord(float counts, float total) {
        float per = (counts / total) * 100;
        return per;
    }
}