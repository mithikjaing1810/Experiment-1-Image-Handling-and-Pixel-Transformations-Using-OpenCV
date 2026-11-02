# ==============================================================================
# Name: Mithik Jain
# Reg No: 212224240087
# Experiment 1: Image Handling and Pixel Transformations Using OpenCV
# ==============================================================================

import os
import cv2
import matplotlib.pyplot as plt

def main():
    image_filename = 'Qno. 1.jpg' if os.path.exists('Qno. 1.jpg') else 'images.jpg'
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)

    # --------------------------------------------------------------------------
    # Step 1: Read and Display an Image
    # --------------------------------------------------------------------------
    img = cv2.imread(image_filename, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "step1_original.png"))
    plt.close()

    # --------------------------------------------------------------------------
    # Step 2: Draw Shapes and Add Text
    # --------------------------------------------------------------------------
    image = cv2.imread(image_filename)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, c = img_rgb.shape

    # 1. Line
    line_img = cv2.line(img_rgb.copy(), (0, 0), (w, h), (255, 0, 0), 2)
    plt.figure(); plt.imshow(line_img); plt.title("Line"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step2_line.png")); plt.close()

    # 2. Circle
    center_x, center_y = w // 2, h // 2
    circle_img = cv2.circle(img_rgb.copy(), (center_x, center_y), 150, (255, 0, 0), 10)
    plt.figure(); plt.imshow(circle_img); plt.title("Circle"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step2_circle.png")); plt.close()

    # 3. Rectangle
    rectangle_img = cv2.rectangle(img_rgb.copy(), (0, 0), (w, h), (0, 0, 255), 10)
    plt.figure(); plt.imshow(rectangle_img); plt.title("Rectangle"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step2_rectangle.png")); plt.close()

    # 4. Text
    text_img = cv2.putText(img_rgb.copy(), "OpenCV Drawing", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    plt.figure(); plt.imshow(text_img); plt.title("Text"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step2_text.png")); plt.close()

    # --------------------------------------------------------------------------
    # Step 3: Color Space Conversion
    # --------------------------------------------------------------------------
    image = cv2.imread(image_filename)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 1. HSV
    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
    plt.figure(); plt.imshow(image_hsv); plt.title("HSV Image"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step3_hsv.png")); plt.close()

    # 2. Grayscale
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    plt.figure(); plt.imshow(image_gray, cmap='gray'); plt.title("Grayscale Image"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step3_gray.png")); plt.close()

    # 3. YCrCb
    image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)
    plt.figure(); plt.imshow(image_ycrcb); plt.title("YCrCb Image"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step3_ycrcb.png")); plt.close()

    # 4. HSV back to RGB
    image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)
    plt.figure(); plt.imshow(image_hsv_to_rgb); plt.title("HSV to RGB Image"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step3_hsv_to_rgb.png")); plt.close()

    # --------------------------------------------------------------------------
    # Step 4: Pixel Manipulation
    # --------------------------------------------------------------------------
    image = cv2.imread(image_filename)
    pixel_val = image[100, 100]
    print(f"Pixel value at (100, 100): {pixel_val}")

    image[200, 200] = [255, 255, 255]
    image[200:450, 200:450] = [255, 255, 255]

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure(); plt.imshow(image_rgb); plt.title("Image with 300x300 White Block"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step4_pixel_manipulation.png")); plt.close()

    # --------------------------------------------------------------------------
    # Step 5: Image Resizing
    # --------------------------------------------------------------------------
    image = cv2.imread(image_filename)
    h, w, c = image.shape
    resized_image = cv2.resize(image, (w // 2, h // 2))
    resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    plt.figure(); plt.imshow(resized_image_rgb); plt.title("Resized Image (Half Size)"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step5_resized.png")); plt.close()

    # --------------------------------------------------------------------------
    # Step 6: Image Cropping
    # --------------------------------------------------------------------------
    image = cv2.imread(image_filename)
    roi = image[50:350, 50:350]
    roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

    plt.figure(); plt.imshow(roi_rgb); plt.title("Cropped Region of Interest (ROI)"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step6_cropped.png")); plt.close()

    # --------------------------------------------------------------------------
    # Step 7: Image Flipping
    # --------------------------------------------------------------------------
    image = cv2.imread(image_filename)
    flipped_horizontally = cv2.flip(image, 1)
    flipped_horizontally_rgb = cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB)
    plt.figure(); plt.imshow(flipped_horizontally_rgb); plt.title("Flipped Horizontally"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step7_flipped_horizontally.png")); plt.close()

    flipped_vertically = cv2.flip(image, 0)
    flipped_vertically_rgb = cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB)
    plt.figure(); plt.imshow(flipped_vertically_rgb); plt.title("Flipped Vertically"); plt.axis('off'); plt.tight_layout(); plt.savefig(os.path.join(output_dir, "step7_flipped_vertically.png")); plt.close()

    # --------------------------------------------------------------------------
    # Step 8: Save the Final Modified Image
    # --------------------------------------------------------------------------
    cv2.imwrite('final_modified_image.jpg', flipped_vertically)
    print("Saved modified image to 'final_modified_image.jpg'")

if __name__ == '__main__':
    main()
