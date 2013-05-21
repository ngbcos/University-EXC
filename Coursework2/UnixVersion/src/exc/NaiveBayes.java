package exc;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class NaiveBayes {
    
    private NaiveBayes() {
        // Non-instantiable.
    }
    
    /**
     * 'Trains' the naive bayes on a training file. Does not do full training, merely returns
     * a map of features to feature counts.
     * 
     * A trick is used to encode features with the same text. Whole-word features are left as
     * normal, but prefix features (e.g. first 2 letters) have a space appended to them, and 
     * suffix features (e.g. last 2 letters) have a space pre-pended to them.
     * 
     * @param trainingFile the file to train on
     * 
     * @throws IOException if an {@link IOException} was encountered when reading the file
     */
    public static Map<String, FeatureCount> train(File trainingFile) throws IOException {
        Map<String, FeatureCount> featuresMap = new HashMap<String, FeatureCount>();
        
        BufferedReader in = new BufferedReader(new FileReader(trainingFile));
        
        String line;
        while ((line = in.readLine()) != null) {
            String[] words = line.split("\\s+");
            
            for (String word : words) {
                boolean isUppercase = isUppercase(word);
                
                String wordFeatures[] = new String[5];
                wordFeatures[0] = word.toLowerCase();
                wordFeatures[1] = getLastNLetters(word, 2);
                wordFeatures[2] = getLastNLetters(word, 3);
                wordFeatures[3] = getFirstNLetters(word, 2);
                wordFeatures[4] = getFirstNLetters(word, 3);
                
                for (String feature : wordFeatures) {
                    // Skip non-existant features.
                    if (feature == null) {
                        continue;
                    }
                    
                    if (!featuresMap.containsKey(feature)) {
                        featuresMap.put(feature, new FeatureCount(feature));
                    }
                    if (isUppercase) {
                        featuresMap.get(feature).incrementUpperCount();
                    } else {
                        featuresMap.get(feature).incrementLowerCount();
                    }
                }
                
            }
        }
        return featuresMap;
    }

    /**
     * Classifies words from an input stream with regards to a set of training features.
     * 
     * @param in the input stream to read from
     * @param features the set of training features
     * 
     * @return a list of capitalized/uncapitalized words
     */
    public static List<String> classify(InputStream in, Map<String, FeatureCount> features) {
        List<String> classifiedWords = new ArrayList<String>();
        
        Scanner scanner = new Scanner(in);
        
        while (scanner.hasNextLine()) {
            String word = scanner.nextLine();
            
            String wordFeatures[] = new String[5];
            wordFeatures[0] = word;
            wordFeatures[1] = getLastNLetters(word, 2);
            wordFeatures[2] = getLastNLetters(word, 3);
            wordFeatures[3] = getFirstNLetters(word, 2);
            wordFeatures[4] = getFirstNLetters(word, 3);
            
            float probUpper = 1;
            float probLower = 1;
            
            for (String feature : wordFeatures) {
                if (!features.containsKey(feature)) {
                    continue;
                }
                
                FeatureCount featureCount = features.get(feature);
                
                probUpper *= featureCount.getUpperProbability();
                probLower *= featureCount.getLowerProbability();
            }
            
            if (probLower >= probUpper) {
                classifiedWords.add(word);
            } else {
                classifiedWords.add(capitalize(word));
            }
        }
        return classifiedWords;
    }

    /**
     * Checks if a given string is uppercase. A string is taken as being
     * uppercase if *any* character within it is uppercase.
     * 
     * @param word the string to check for uppercase-ness
     */
    private static boolean isUppercase(String word) {
        for (char ch : word.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Extracts the last n letters from a word, or null if the word length is less than n.
     * 
     * @param word the word to extract characters from
     */
    private static String getLastNLetters(String word, int n) {
        if (word.length() < n) {
            return null;
        }
        return word.substring(word.length() - n, word.length()).toLowerCase();
    }

    /**
     * Extracts the first n letters from a word, or null if the word length is less than n.
     * 
     * @param word the word to extract characters from
     */
    private static String getFirstNLetters(String word, int n) {
        if (word.length() < n) {
            return null;
        }
        return word.substring(0, n).toLowerCase();
    }

    /**
     * Capitalizes a word. Assumes that the entire word is lowercase to begin with.
     * 
     * @param word the word to capitalize
     */
    private static String capitalize(String word) {
        return word.substring(0, 1).toUpperCase() + word.substring(1);
    }
}
