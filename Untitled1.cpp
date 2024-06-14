#include <iostream>
#include <filesystem>
#include <opencv2/opencv.hpp>

int main() {
    // Create a directory to save images if it doesn't exist
    std::filesystem::path image_directory = "images";
    if (!std::filesystem::exists(image_directory)) {
        std::filesystem::create_directory(image_directory);
    }

    // Initialize the camera
    cv::VideoCapture cap(0);

    std::cout << "Press 'c' to capture an image and 'q' to quit." << std::endl;

    while (true) {
        cv::Mat frame;
        bool ret = cap.read(frame);
        if (!ret) {
            std::cerr << "Failed to grab frame" << std::endl;
            break;
        }

        cv::imshow("Capture Image", frame);

        int key = cv::waitKey(1);
        if (key % 256 == 'c') {
            // Press 'c' to capture an image
            std::filesystem::path img_name = image_directory / "captured_image.jpg";
            cv::imwrite(img_name.string(), frame);
            std::cout << "Image saved: " << img_name << std::endl;
        } else if (key % 256 == 'q') {
            // Press 'q' to quit the program
            std::cout << "Quitting..." << std::endl;
            break;
        }
    }

    // Release the camera and close the window
    cap.release();
    cv::destroyAllWindows();

    return 0;
    
}

