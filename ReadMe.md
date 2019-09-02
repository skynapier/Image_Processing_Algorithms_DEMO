# [Quetion Introduction File](/project1.pdf)

## Part 1.1  Edge Detection

### Procedure:


	          +1  0  -1 	       			    +1   +2   +1
    Row mask =+2  0  -2                      Col mask =  0    0    0   
 	          +1  0  -1 	       		           -1   -2   -1
 	        	
1. Define two matrix (masks) as specified by the sobel operator 
2. Using OpenCV to read image into 2d array.
3. Get one central pixel and generate pixel matrix by include peripheral pixels the on the original image, if the peripheral pixels do not exist then fill 0 instead.
4. Apply convolution using row and col mask to get s1 for row convolution and s2 for col convolution
5. Replace the pixel on the output image by  s= ¡Ì(¡¼s1¡½^2+ ¡¼s1¡½^2 )
6. Repeat step 3 and 4 until all the pixels have count the convolution. 


### Part 1.2  Noise Cancellation

Procedure are similar with Edge Detection, replace the convolution mask.

                    1/9  1/9  1/9 	       			
    Mean Filter =	1/9  1/9  1/9                     Median Filter = The mean across the convlution matrix
                    1/9  1/9  1/9 	       			


### Part1.3  Image Enhancement

This part using Laplacian operator for the convolution mask.

                    0  -1   0 	       			
    Mean Filter =	-1   5  -1                   
                    0  -1   0 


### Part 2.1 Mining Space Images:
#### The Procedure of Part2.1:
1.	Apply 3*3 mean filter to smooth the image
2.	Find a proper threshold by some method
3.	If the pixel is greater than the threshold, turn it to white on output image, otherwise turn to black

The purpose in this part is find the only large galaxies in the map. The threshold is for classify that the pixel belongs to the large galaxies or not. 
I construct one method to find this threshold. I count the total frequency for every pixel in the smooth graph. Because of the main pixel in this 
graph is black, and our pixels could show as a range of numbers. For example, the majority color of this graph is A which could explain as a number
and the majority color of the larger galaxies is number B. the span of |A-B| near the color range like 255 in RGB graph. If the galaxies are more like 
near us then the value of that pixels are distributing on B, vice versa. 

In this case, the distribution of A and B might have a small overlap. My method is picking a range X and start at X+1 at the color range. Select two 
groups, one for left hand side with size of X compare with right hand side also with size X. Compare with the summary of two groups S1 and S2. 
If S1/S2 is in (1.8 2) then that means have a enough difference between two sides. i.e. if two hand side have a huge difference then the S1/S2 will 
be huge, if the two-hand side have a tiny difference then the S1/S2 will near 1.

#### Pseudocode:
1.	Count the frequency on a color range of all pixels.
2.	Set threshold = ¡Þ
3.	Set a range X of pick pixels by two sides
4.	Start at X + 1 at color range get left-hand side list and right-hand side list with size X.
5.	Calculate the sum value of two sets S1 and S2 for left and right.
6.	If S1/S2 > 1.8 and S1/S2 < 2 and S1/S2 < threshold then threshold = X
7.	Return threshold

The threshold by my own algorithm is 86 for this image. Therefore, if a pixel is greater than 86 then write white(255) on output image, otherwise write black(0) on output image.

If the graph without smooth then the threshold would be lower, and small stars would not be removed in the graph. The output image would contain small white dots than the current output.

People could use other domain knowledge like astronomy to tune the threshold subjectively to achieve a better answer. For example, because I do not know what size that the large galaxies are. 
Some galaxies that I think is small might different with the other experts¡¯ opinion. Changing the S1/S2 range would get different result. If increase the upper bound then will get more galaxies, vice versa. 

