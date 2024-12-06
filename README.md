# Image-Quantizer
This image quantizer reduces the number of colors within an image. The program makes use of the [K-Means++](https://en.wikipedia.org/wiki/K-means%2B%2B) clustering algorithm. The project was inspired by my [Diamond Painting Generator](https://github.com/EvanC8/Diamond-Painting-Generator) that makes use of a third party quantization method. Try it out with your own images!

<img src="https://github.com/EvanC8/Image-Quantizer/blob/main/starrynight.jpg?raw=true" width="200"> <img src="https://github.com/EvanC8/Image-Quantizer/blob/main/quantized_starrynight.jpg?raw=true" width="200"> <br>
<img src="https://github.com/EvanC8/Image-Quantizer/blob/main/dominate_colors_starrynight.jpg?raw=true" width="404">

Quantization of the <i>Starry Night</i> painting with 24 colors (24 clusters)

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#how-it-works">How it works</a>
      <ul>
        <li><a href="#clustering-method">Clustering Method</a></li>
        <li><a href="#interpreting-clusters">Interpreting Clusters</a></li>
        <li><a href="#k-means++-improvement">K-Means++ Improvement</a></li>
      </ul>
    </li>
    <li><a href="#next-steps">Next Steps</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

# Installation
* Clone the repo
   ```sh
   git clone https://github.com/EvanC8/Image-Quantizer.git
   ```
# Usage
1. Download project
2. Upload image to project directory
3. Insert image name into `Quantize.py`
4. Run `Quantize.py`

# How it works

### Clustering Method
The program utilizes the `K-Means++ clustering algorithm` to determine a specified number of dominate colors within the image to use as a palette to then quantize the image. 

<b>K-Means Clustering</b><br>
In an uploaded image, each pixel's RGB color value represents a point in 3D space. Within this color space, cluster centroid locations are chosen at random. "k" number of specified centroids are set. After adding a centroid, each pixel's parent centroid is set to be its closest neighboring centroid. This is what forms the clusters of colors. 

### Interpreting Clusters
Once "k" number of clusters have been formed, the colors within each cluster are averaged together to produce one dominant color of the image. 

<b>Mapping Dominant Colors to Image</b><br>
Each pixel in the original image is replaced with the dominant color in closest proximity to the pixel's original color. The quanitized image has been produced.

### K-Means++ Improvement
A downside to the K-Means base approach is that cluster centroids are determined at random in the 3D color space. Consequently, it is likely for two centroids to be chosen right next to eachother, which could result in a lack of variation between dominate_colors and could also leave out some dominate colors. The K-Means++ approach mitigates this issue by making use of weighted probabilities. Instead of choosing centroids completely at random, a `Cumulative Distribution Function` (CDF) is used. 

<b>Using a Cumulative Distribution Function</b><br>
After each centroid is added, each pixel is assigned a weight determined by its euclidean distance to its nearest centroid. To determine the next centroid, the weights of all pixels are sumed to a total weight and a random number is chosen between 0 and the total weight. Using an efficient binary search algorithm, the random number can be traced back to a new color location to be set as a centroid. Because of how weights are determined, color farther apart from centroids are favored in determining each new centroid. A more constrasting quantized image is produced.


# Next Steps
* Optimize algorithm for faster performance with larger images
* Explore other methods of creating and averaging clusters to produce more contrasting quanitization results

# License
Destributed under the MIT License. See `LICENSE.txt` for more information.

# Contact
Evan Cedeno - escedeno8@gmail.com

Project Link: [Image Quantizer](https://github.com/EvanC8/Image-Quantizer)

