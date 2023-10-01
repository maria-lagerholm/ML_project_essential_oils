# AI-Driven Classification and Bioactivity Analysis of Essential Oil-Producing Plants

## Table of Contents
- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Data Preprocessing](#data-preprocessing)
- [Clustering Analysis](#clustering-analysis)
- [Visualization](#visualization)
- [Conclusion](#conclusion)

## Introduction

In a world where we often reach for a pill for every ailment, the importance of plants might not be immediately obvious. However, it’s essential to remember that the first medicines were inspired by the natural defenses of plants, fungi, and bacteria. These living things have evolved to protect themselves from diseases with unique compounds, called secondary metabolites, which have much to teach us.

Essential oils, which have become popular for their varied uses in areas like medicine, cosmetics, and the food industry, are more than just pleasant scents. They are concentrated versions of plants, carrying not only their fragrance but also their beneficial and therapeutic properties. The study being discussed here categorizes plants by looking at the unique chemical profiles of their essential oils, helping to increase our understanding of the complicated mix of compounds within as well as their hidden simillarities.

The potential within plants continues to be a source of fascination and discovery, and with the use of Artificial Intelligence (AI), there are even more opportunities to learn and benefit from the natural world around us.



### Rationale
Taking steps to categorize plants based on the makeup of their essential oils is a meaningful advance towards uncovering the possible uses and health benefits these oils may hold. This method of classification shines a light on the unseen similarities between various plant species and the oils they yield. By adopting this approach, we gain valuable insights into how we might use these essential oils and their individual components, establishing a basis for their use in different areas such as aromatherapy, pharmaceuticals, and natural remedies.

Furthermore, this study provides important information about specific compounds found within the oils, known as secondary metabolites. Identifying which of these compounds are biologically active is crucial, as it paves the way for additional research and development. These active compounds can be further produced and enhanced through various methods, either using traditional chemical processes or through newer, innovative biotechnological strategies. This includes the use of genetically modified organisms (GMOs) that are engineered to produce these compounds efficiently and on a larger scale, meeting the demands of the pharmaceutical industry.




### Objectives
- **Part 1. Plant Classification**: The first objective is to classify plants based on the chemical composition of their essential oils, gaining more insight into their similarities. Traditional plant classification methods often rely on morphological features (the form and structure of plants), physiological properties (how plants function), and genetic data. 

By focusing on the chemical composition of essential oils, this study aims to offer a complementary perspective to existing classification methods. It can reveal previously unrecognized connections between different plant species, providing a deeper understanding of their potential uses.

This chemical-based classification approach is particularly relevant as it can identify specific compounds or groups of compounds that are responsible for the plants’ therapeutic or aromatic properties. It allows for a more precise and targeted application of these plants and their derived products, facilitating the development of new treatments, flavors, or scents.

- **Part 2: Understanding Biological Activities**: Part 1 of this study lays the groundwork for the second objective which is exploration of the relationships between the chemical makeup of essential oils and their biological effects. With the aid of Artificial Intelligence (AI) and a deep dive into decades of research, we aim to gain a clearer understanding of which specific compounds in essential oils are crucial for particular biological activities. This is aimed at creating a comprehensive resource that brings together the knowledge acquired over the past 50 to 100 years of scientific investigation into essential oils. By doing so, we enhance our ability to accurately predict the potential uses and biological effects of essential oils and the compounds within them, providing a reliable guide for their application in various fields.



### Significance

This study holds importance for both scientists and everyday individuals interested in the potential of plants and their essential oils. It unveils hidden connections between various plants by closely examining the chemical makeup of their oils, providing new, practical insights that are applicable in medicine, cosmetics, and even in our kitchens.

Moreover, the research serves as a bridge, connecting valuable knowledge gathered over decades, offering a resource for anyone interested in biological activities of plants. 

Incorporating advanced technology, like Artificial Intelligence (AI), the study aims at understanding of chemical profiles of essential oils and their biological activities, opening doors to innovative treatments and applications. The significance of this study lies in its ability to apply  innovative technology on scientific knowledge, providing new ways to explore and utilize the potential of plants for everyone’s benefit.





### Data Collection
- Data is extracted from essentialoils.org/db using Python’s requests library. Headers, including a cookie and token for authentication, are set up to mimic a real browser request. The code then iterates over a range of IDs (from startidx to endidx), constructing a URL for each ID, sending a GET request to the constructed URL, and collecting the server’s response.

Check out the [Script](https://github.com/danielzmod/webscrape/blob/main/scrape.py)!

> **Disclaimer**: The terms and conditions should still be verified as well as the validity of the data.

## Data Preprocessing
- Standard techniques were employed, including transposing the data, removing duplicate entries, and substituting NaN values with zeros.


## Clustering Analysis
### Objective 
Identify clusters of plants based on their chemical compositions using clustering algorithms.

### Methodology
- **K-means Clustering**: The use of clustering algorithms such as K-means or DBSCAN to identify groups or clusters of plants based on their chemical compositions can help identify similarities and differences among different plant species. Find hidden structures in the data that are not immidiately availible. K-means - groups of simmilar instances - the closest centroid to each data sample.
- **Euclidean Distance**: Elaboration on why Euclidean distance is suitable compared to other distance measures (e.g., Manhattan, Cosine, etc.). Euclidean distance is effective in identifying clusters in a dataset where features have similar scales (0 to 1, in our case), making it suitable for our chemical composition data.
- Similarity score is 1 - Euclidean Distance, so that a higher score corresponds to a higher similarity between plants.


### Clustering
The data is loaded from a CSV file, where each row represents a different plant (or essential oil), and the columns represent different chemical compositions. The code iteratively applies K-Means clustering with a varying number of clusters (from min_clusters to max_clusters). For each iteration, it computes the Silhouette Score to evaluate the quality of the clustering. The number of clusters that gives the highest Silhouette Score is selected as the optimal number. With the optimal number of clusters determined, K-Means clustering is applied again to assign each plant to a specific cluster. For each cluster, the code extracts the plants assigned to it, calculates pairwise Euclidean distances between them, converts these distances to similarities, and saves this information to CSV files.

## Visualization
### Heatmaps
- Generation of heatmaps for similarity scores between pairs of plants.
- Heatmap Generation:
The code loads the previously saved similarity data for each cluster.
Title Generation: It generates a title for each heatmap, including the cluster number and the common families of plants within the cluster.
Each heatmap is saved as a PDF file.
![Cluster_visualization](https://i.imgur.com/6UHnICL.jpg)

### Chemical Contribution Analysis (Bar Plots)
- The code analyzes pairs of plants within each cluster, filters those with high similarity, extracts and ranks their common chemicals, removes duplicates, and saves the results. Each cluster's results are saved in a separate CSV file within a designated directory for that cluster. Next the code identifies highly similar plant pairs, extracts and organizes their chemical compositions, and prepares the data for visualization. It then generates bar plots to visually represent and compare the main chemicals and their amounts in each plant pair.
- ![Common chemicals](https://i.imgur.com/4ESnlvR.png[)

- The next code creates a heatmap for each CSV file, with each row in the heatmap corresponding to a plant and each column corresponding to a chemical. The color of each cell in the heatmap corresponds to the value in the CSV file for that plant and chemical. The heatmaps are then saved as PDF files. 

- Heatmap representing main chemicals and their amounts in similar plants.
- ![Heatmap](https://i.imgur.com/eqe439w.png)

### Additional steps

- Biological activities data extraction is coming soon.

## Conclusion
- Summary of findings and conclusions drawn from the study coning soon.

## References
- List of references coming soon

***  I added all .json files into gitignore all for data protection as well as chemicals_data.csv and chemicals_data_clean.csv
