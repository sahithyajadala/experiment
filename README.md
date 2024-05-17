## Bounding_box

It is used to crop the image and draw bounding boxes on image using the argparse

## instalisation

install PIL and argparse by using pip

       pip install Pillow
       pip install argparse

Install the required dependencies using pip

## usage

    pip install -r requirment.txt

## Explanation

place the csv file containing the images and give the image dir path 
creat a directory by using os.mkdir for store the output. Paths are passing through the terminal
parser.add_argument("--image_path", help = "Enter the path of your image")
parser.add_argument("--csv", help = "your csv file path , which has bounding box values")
parser.add_argument("--out_dir", help = "name of output directory")
args = parser.parse_args() is used to save the arguments

image_path : path to the input image
csv : Path to the CSV file containing bounding box coordinates.
out_dir: Name of the output directory where processed images will be saved.



Argument Parsing:

    The script uses argparse to parse command-line arguments for specifying the input image, CSV file, and output directory.




functions draw_boxes for used to draw the bounding boxes
draw.rectangle([left, top, right, bottom], outline="red")

draw_crop is used to crop the images
cropped_img = image.crop((left, top, right, bottom))
          
This method takes 5 mandatory parameters:

    image: A numpy array, channel last (ie. height x width x colors) with channels in BGR order (same as openCV format).
    left: A integer representing the left side of the bounding box.
    top: A integer representing the top side of the bounding box.
    right: A integer representing the right side of the bounding box.
    bottom: A integer representing the bottom side of the bounding box.



output_dir = "/home/sahitya-jadala/Downloads/7622202030987_with_boxes"
this dir is used to save the output

input
![7622202030987_f306535d741c9148dc458acbbc887243_L_487](https://github.com/sahithyajadala/exper2/assets/169046012/12d92a80-aa51-4f11-94d5-c00e9003b5e8)

output
![full_7622202030987_f306535d741c9148dc458acbbc887243_L_533](https://github.com/sahithyajadala/exper2/assets/169046012/68a74e9c-b61b-41d9-8073-a406fdc3fc23)

## Histogram

  This script is used to convert the image to graph representation using the argparse

## Installation
 install opencv,numpy,matplotlib,argparse by using pip
      pip install opencv-python
numpy
       pip install numpy
       
matplotlib

       pip install matplotlib
       pip install argparse
## Usage

Run the script "histogram.py"
parser.add_argument("--image_path", help = "Enter the path of your image")
parser.add_argument("--output_path", help = "name of output path")
give input path of image passing through the terminal

give the output path to save the image. passing through the terminal.
The script will generate a histogram plot for each color channel and display it.

## Explanation
img = cv.imread(args['image_path']) Reads the input image.
give the output path to save the image.
cv.calcHist() :Calculate histograms for each color channel.
plt.plot() : Plots the histograms using Matplotlib.

## Example
Input
![shizuka](https://github.com/sahithyajadala/expr3/assets/169046012/5de4e999-2253-4078-9ff5-aeb0822333ee)

output


![output](https://github.com/sahithyajadala/expr3/assets/169046012/c91ada1f-5a20-4e4c-bea6-065b87e0cd7f)


 ## Iteration

 This Python script calculates the sum of a number with its previous number in a loop and prints the result. bBy using the argparse

 ## instalisation

install  argparse by using 

       pip install argparse 

 ## Usage

 This script is used to print the current number,previous number and print the sum of two numbers in the range
       
       pip install -r requirment.txt

 ## Explanation
 
    The script iterates through numbers from 0 to 9 using a for loop.
    For each iteration, it calculates the sum of the current number and the previous number.
    It prints the current number, the previous number, and their sum. the values are passing through the terminal by using the argument of argparse. it gives the output for given range.

## Output


Current number 0 Previous Number 0 is 0

Current number 1 Previous Number 0 is 1

Current number 2 Previous Number 1 is 3

Current number 3 Previous Number 2 is 5

Current number 4 Previous Number 3 is 7

Current number 5 Previous Number 4 is 9

Current number 6 Previous Number 5 is 11

Current number 7 Previous Number 6 is 13

Current number 8 Previous Number 7 is 15

Current number 9 Previous Number 8 is 17

## Webcam(video capture)

This script is used to capture the video from webcam by using opencv and argparse

## Installation

install opencv and argparse by using pip

    pip install opencv-python
    pip install argparse

## Usage

define the argparse arguments to give the width and height of the frame to capture the video

parser = argparse.ArgumentParser()
parser.add_argument("--WIDTH",type=int,help="enter width value")
parser.add_argument("--HEIGHT",type=int,help="enter height value")
parser.add_argument("--SIZE: WIDTH,HEIGHT")
args = parser.parse_args() is used to save the arguments

     pip install -r requirment.txt

## Explanation


define the argparse arguments to give the width and height of the frame to capture the video
 parser.add_argument("--WIDTH",type=int,help="enter width value")
  

parser.add_argument("--HEIGHT",type=int,help="enter height value")
  To give the height of the frame

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fourcc is used to store the video in "MJPG" 

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

out = cv2.VideoWriter('web_video1.avi', fourcc, 20.0, size)
out is used to store the video web_video1.avi

using while loop to capture the video frame
cap = cv2.VideoCapture(0) 

The webcam stream will open, and you'll see the live video displayed in a window.

To exit the program, press the 'q' key. This will close the video window and terminate the script.

## output:

https://github.com/sahithyajadala/experiment/assets/169046012/b75f4f64-9212-4b80-8474-2ac4559baf5e
















   
