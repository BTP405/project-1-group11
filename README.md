## 1. Project Title and Description
    - Title: Map-Based Interactive Region Selection
    - Description: The map-based interactive region selection project allows users to interactively 
                   mark and save regions of interest (ROIs) on a map displayed via a webcam feed. The goal of this project 
                   is to make chores like locating and marking particular locations on a map for different purposes easier. 
                   Including applications for augmented reality, object tracking, and spatial analysis.
## 2. Installation
    - Dependencies:OpenCV, NumPy, Pickle
    - Installation Instructions: Install the required dependencies using pip:
                                 pip install opencv-python numpy
                                 A connection to the webcam is required for the full implementation
## 3. Usage
    - Examples: Run get_map.py to mark four corner points on a map displayed through a webcam feed.
                Run get_countries.py to mark and save regions of interest (ROIs) on the map using mouse clicks.
    - Configuration: Modify the camera ID, resolution, and file paths in the scripts according to your setup and requirements.
## 4. Features
    - List of Features: Mark and save corner points for perspective transformation.
                        Mark and save polygons representing regions of interest on a map.
                        Visualize marked regions on the map in real-time.
## 5. Contributing
    - Guidelines: Fork the repository, make your changes, and submit a pull request for review.
    - Code Style: N/A
## 6. Credits
    - Authors: Tony Kim, Yash, Yash Atulbhai Akbari, Bajpayee Aum Shekhar
    - Acknowledgments: N/A

## 7. Packagin and Docker
    -step 1 : Clone the repository
    -step 2 : Navigate to project directory
    -step 3 : run command #docker run -it docim (container name - docim)
    
## 8. Unit Testing
Step 1 Unit Test:
    -test_click_points: This test checks the functionality of clicking points on the map. 
     It simulates mouse clicks on a mock image and asserts that the correct number of points are selected and saved.
    -test_warp_image: This test verifies the functionality of warping an image based on provided points. 
     It creates mock points and an image, then asserts that the image is warped correctly.

Step 2 Unit Test:
        -test_mark_polygons: This test evaluates the functionality of marking polygons for countries. 
         It creates a mock image and simulates mouse clicks for each country, then asserts that the polygons are marked correctly.
        -test_save_load_polygons: This test checks the saving and loading functionality of polygons. 
         It saves mock polygons to a file, then loads them back and asserts that the loaded polygons match the original ones.

Step 3 Unit Test:
        -test_get_finger_location: This test verifies the functionality of getting the location of the index finger tip in the warped image. 
         It creates a mock image and warped image, then calls the function and asserts the result.
        -test_create_overlay_image: This test evaluates the functionality of creating an overlay image with marked polygons based on the warped finger location. 
         It creates mock polygons and a finger location, then calls the function and asserts the result.

These unit tests cover various functionalities of each step in the project, ensuring that they behave as expected and providing confidence in the correctness of the code.
## 9. License
    - License Information: N/A
## 10. Additional
