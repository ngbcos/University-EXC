package exc;

/**
 * A count of lower and upper case instances for a feature string.
 */
public class FeatureCount {
    private String feature;
    private int lowerCount;
    private int upperCount;
    private float upperProbability;
    private float lowerProbability;
    private boolean probabiltiesCached;

    public FeatureCount(String feature) {
        this.feature = feature;
        
        this.lowerCount = 0;
        this.upperCount = 0;
        this.probabiltiesCached = false;
    }
    
    public void incrementUpperCount() {
        upperCount++;
        probabiltiesCached = false;
    }
    
    public void incrementLowerCount() {
        lowerCount++;
        probabiltiesCached = false;
    }
    
    public String getFeature() {
        return feature;
    }
    
    public float getUpperProbability() {
        if (!probabiltiesCached) {
            // Compute both, so that the cache can be refreshed.
            calculateProbabilities();
        }
        return upperProbability;
    }
    
    public float getLowerProbability() {
        if (!probabiltiesCached) {
            // Compute both, so that the cache can be refreshed.
            calculateProbabilities();
        }
        return lowerProbability;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((feature == null) ? 0 : feature.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        FeatureCount other = (FeatureCount) obj;
        // FeatureCount's are equal based on their feature name, 
        // not their upper/lower counts.
        if (feature == null) {
            if (other.feature != null)
                return false;
        } else if (!feature.equals(other.feature))
            return false;
        return true;
    }
    
    /**
     * Calculates and sets the upper and lower probabilities, and caches
     * them.
     */
    private void calculateProbabilities() {
        if (lowerCount + upperCount == 0) {
            upperProbability = 0.0f;
            lowerProbability = 0.0f;
        }
        
        upperProbability = (float) upperCount / (float) (lowerCount + upperCount);
        lowerProbability = 1 - upperProbability;
        probabiltiesCached = true;
    }
}
