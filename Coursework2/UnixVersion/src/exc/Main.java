package exc;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Map;

public class Main {
    
    private Main() { 
        // Non-instantiable.
    }
    
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java src.Main training_data");
            return;
        }
        
        File trainingFile = new File(args[0]);
        if (!trainingFile.exists() || !trainingFile.canRead()) {
            System.err.println("Unable to open training file '" + args[0] + "' for reading.");
            return;
        }
        
        try {
            Map<String, FeatureCount> features = NaiveBayes.train(trainingFile);            
            List<String> output = NaiveBayes.classify(System.in, features);
            
            for (String word : output) {
                System.out.println(word);
            }
        } catch (IOException e) {
            System.err.println("IOException when trying to read from the training file:");
            System.err.println(e.getMessage());
            return;
        }
    }
}
