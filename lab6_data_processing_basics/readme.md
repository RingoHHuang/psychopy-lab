# Lab 6 - More Data!

Today, we will learn to process each subject's data, aggregate all the subject's data into one data frame, and then visualize the grouped data!

To follow along, please download all the materials (including the .csv data files) from the Week 6 Lab folder.

## Processing

#### Steps: 
1. **Import modules**


```python
import pandas as pd
```

2. **Read in data as a data frame**


```python
filename = 'sub-101_fa-5_redlight_greenlight.csv'

subject_df = pd.read_csv(filename)

subject_df
```


```python
cr_la = (subject_df["resp"].isna()) & (subject_df["trial_type"] == "nogo")

cr_la
```


```python
subject_df.loc[hit_la, "sdt_label"] = "hit"
subject_df.loc[cr_la, "sdt_label"] = "cr"
subject_df
```

3. **Test whether each row (i.e., trial) is a "HIT", "FA", "MISS", or "CR"**. We will do this by creating logical arrays. To test if a value is NaN, use `.isna`


```python
# First, let's generate logical arrays for each signal detection label:
hit_la = (subject_df["resp"] == "space") & (subject_df["trial_type"] == "go")
fa_la = (subject_df["resp"] == "space") & (subject_df["trial_type"] == "nogo")
cr_la = (subject_df["resp"].isna()) & (subject_df["trial_type"] == "nogo")
miss_la = (subject_df["resp"].isna()) & (subject_df["trial_type"] == "go")

# Optionally, add a column called sdt_label, which labels each trial
subject_df.loc[hit_la, "sdt_label"] = "hit"
subject_df.loc[fa_la, "sdt_label"] = "fa"
subject_df.loc[cr_la, "sdt_label"] = "cr"
subject_df.loc[miss_la, "sdt_label"] = "miss"

```


```python
subject_df["trial_type"] == 'go'
```

4. **Calculate Hit Rate and FA Rate**


```python
# Count the number of hits and FAs using the logical arrays
hit_count = sum(hit_la)
fa_count = sum(fa_la)

# Option 2, count the number of hits and FAs using the sdt_label column:


# Count the number of nogo trials or go trials
go_count = sum(subject_df["trial_type"] == 'go')
nogo_count = sum(subject_df["trial_type"] == 'nogo')

# Calculate Hit Rate as hit_count/go_count; do same for fa_rate (fa_count/nogo_count)
hit_rate = hit_count/go_count
fa_rate = fa_count/nogo_count
```

5. **Calculate $d_{prime}$ and $\lambda$ assuming equal variance Gaussian model**. For this, you need to install and import the `scipy` library. We can use some of the stats methods to easily get the Z values from probabilities. Documentations for the stats methods here: https://scipy.github.io/devdocs/tutorial/stats.html


```python
import scipy.stats as st

# Convert the hit and fa rates to Z_hit and Z_fa
Z_hit = st.norm.ppf(hit_rate)
Z_fa = st.norm.ppf(fa_rate)

```


```python
# Calculate lambda (Book Eq'n 2.3)
lam = -Z_fa

# Calculate d-prime (Book Eq'n 2.4)
d_prime = Z_hit - Z_fa

```

6. **Calculate bias metrics $log\beta$ and $\lambda_{center}$**


```python
# Calculate lam_center (Book Eq'n 2.5)
lam_center = lam - .5*d_prime

# What's an alternative what to calculate lam_center from Z_hit and Z_fa? (Book Eq'n 2.6)
lam_center = -.5*(Z_fa + Z_hit)

# Calculate log_beta (Book Eq'n 2.10)
log_beta = d_prime*(lam - .5*d_prime)

log_beta
```

Based on these bias metrics, is the subject more biased towards the signal or the noise distribution?

7. **Record the all the metrics you just calculated in a list.** Also include Participant ID and the Condition.

When dealing with strings, you'll often need to parse and pattern match. This falls into the world of **regular expressions** or **RegEx**. Python has a base regex library called `re` (https://docs.python.org/3/library/re.html). We will use this to grab participant id and condition from `filename`.


```python
import re
print(filename)
re.split('',filename)
```


```python
# This is a base python library for regular expressions.
import re

# Extract Participant ID and Condition from the filename
_, sub, _, cond, _, _ = re.split('-|_',filename)

cond
```


```python
# Include sub, cond, and metrics into a list
subject_list = [sub, cond, hit_rate, fa_rate, lam, d_prime, lam_center, log_beta]
subject_list
```

8. **Now, put all the previous steps in a loop!** Loop through all the data files that you collected.

Use glob to find all the _redlight_greenlight.csv files in this directory. This is a simple pattern matching way of retrieving only files that match a certain format.


```python
import glob

data_filenames = glob.glob("*_redlight_greenlight.csv")

data_filenames
```

Simply iterate through each `filename` in `data_filenames` and copy the steps above into the code chunk:


```python
aggregated_list = []
for filename in data_filenames:
    
    # Read filename into a data frame
    subject_df = pd.read_csv(filename)
    
    # First, let's generate logical arrays for each signal detection label:
    hit_la = (subject_df["resp"] == "space") & (subject_df["trial_type"] == "go")
    fa_la = (subject_df["resp"] == "space") & (subject_df["trial_type"] == "nogo")
    cr_la = (subject_df["resp"].isna()) & (subject_df["trial_type"] == "nogo")
    miss_la = (subject_df["resp"].isna()) & (subject_df["trial_type"] == "go")
    
    # Count the number of hits and FAs using the logical arrays
    hit_count = sum(hit_la)
    fa_count = sum(fa_la)

    # Count the number of nogo trials or go trials
    go_count = sum(subject_df.trial_type == 'go')
    nogo_count = sum(subject_df.trial_type == 'nogo')

    # Calculate Hit Rate as hit_count/go_count; do same for fa_rate (fa_count/nogo_count)
    hit_rate = hit_count/go_count
    fa_rate = fa_count/nogo_count
    
    # Convert the hit and fa rates to Z_hit and Z_fa
    Z_hit = st.norm.ppf(hit_rate)
    Z_fa = st.norm.ppf(fa_rate)
    
    # Calculate lambda (Book Eq'n 2.3)
    lam = -Z_fa

    # Calculate d-prime (Book Eq'n 2.4)
    d_prime = Z_hit - Z_fa
    
    # Calculate lam_center (Book Eq'n 2.6)
    lam_center = lam - .5*d_prime

    # Calculate log_beta (Book Eq'n 2.10)
    log_beta = d_prime*(lam - .5*d_prime)

    # Extract Participant ID and Condition from the filename
    _, sub, _, cond, _, _ = re.split('-|_',filename)
    
    # Include sub, cond, and metrics into a list
    subject_list = [sub, cond, hit_rate, fa_rate, lam, d_prime, lam_center, log_beta]
    
    # Append subject_list to aggregated_list
    aggregated_list.append(subject_list)

aggregated_list
```

We now have an `aggregated_list` which is a nested list that contains all of the signal detection metrics for all our participants. Let's put it into a data frame.


```python
# Put aggregated_list in a data frame, specifying column headers
aggregated_df = pd.DataFrame(aggregated_list,
                         columns = ["subject_id", "fa_penalty", "hit_rate", "fa_rate", "lambda", "d_prime", "lambda_center", "log_beta"])

aggregated_df
```


```python
# Let's save this  data frame as a csv
aggregated_df.to_csv('aggregated_data.csv')
```

## Visualization
When it comes to visualizing your data in python, you have *many* options (matplotlib, seaborn, plotly, plotnine). We will use `plotnine` for just a brief demonstration today, because it is based off of `ggplot` packages in R. However, it's more common for pure Python users to learn matplotlib, seaborn, and plotly - so I might cover those later.

### Plot Hit Rate and FA Rate


```python
from plotnine import ggplot, aes, geom_point, geom_col, geom_boxplot

ggplot(aggregated_df) + aes(x="fa_penalty", y="hit_rate") + geom_boxplot() + geom_point()
```


```python
ggplot(aggregated_df) + aes(x="fa_penalty", y="fa_rate") + geom_boxplot() + geom_point()
```

### Plot the bias metrics
How might we predict participants to respond when there's a greater FA penalty? Would they press the spacebar more often or less often?

Which of our two conditions (5-penalty vs 10-penalty) would have a more positive log_beta?


```python
ggplot(aggregated_df) + aes(x="fa_penalty", y="log_beta") + geom_boxplot() + geom_point()
```

# For Next Week:
Next week, I want to cover things that are directly relevant to helping you create your experiment. **If there is something relevant to your project that you would like me to go over next week, please e-mail me and I'll try to incorporate it into next week's lesson plan.**

Here are a couple of topic ideas:
- Simple statistical tests (e.g., correlations, t-tests, anovas)
- Should I create a simple experiment using auditory stimuli?
- Visual stimuli processing? I can cover how I use these image processing software:
    1. XnConvert - great for batch processing (e.g., turn all your images to grayscale; resize; crop; etc.)
    2. Photoshop - more involved but sometimes necessary (e.g., isolate foreground object from background)
- Auditory stimuli processing? 
    1. Audacity - lots of features, but I mainly use it to trim audio files or match volume levels between clips
- Any other requests are welcome! I will do my best to accomodate.

#### In terms of where to get stimuli for your experiment, I have an extensive library of images and some audio stimuli. Here are some that I have:
1. Animals
2. Tools
3. Produce
4. Line drawings (Snodgrass and Vanderwart; Nishimoto)
5. Emotional images (IAPS)
6. BOSS
7. OASIS
8. Lots of random objects
9. Emotional auditory stimuli (IADS)

To find images, you can also use google images (although if you were conducting an IRB-approved study, you would be restricted to images with a Creative Commons license). You can use Pixabay and Wikimedia Commons to search for free and open access images.
