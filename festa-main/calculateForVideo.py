import mediapipe as mp
import numpy as np
import cv2
def rescale_frame(frame, percent=30):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def calculate_angle(point1: list, point2: list, point3: list) -> float:
    angleInDeg = np.abs(np.arctan2(np.array(point3)[1] - np.array(point2)[1], np.array(point3)[0] - np.array(point2)[0]) - np.arctan2(np.array(point1)[1] - np.array(point2)[1], np.array(point1)[0] - np.array(point2)[0]) * 180.0 / np.pi)
    angleInDeg = angleInDeg if angleInDeg <= 180 else 360 - angleInDeg
    return angleInDeg

def extract_important_keypoints(results, important_landmarks: list) -> list:
    landmarks = results.pose_landmarks.landmark

    data = []
    for lm in important_landmarks:
        keypoint = landmarks[mp.solutions.pose.PoseLandmark[lm].value]
        data.append([keypoint.x, keypoint.y, keypoint.z, keypoint.visibility])

    return np.array(data).flatten().tolist()

def analyze_knee_angle(
    mp_results, stage: str, angle_thresholds: list, draw_to_image: tuple = None
):
    """
    Calculate angle of each knee while performer at the DOWN position

    Return result explanation:
        error: True if at least 1 error
        right
            error: True if an error is on the right knee
            angle: Right knee angle
        left
            error: True if an error is on the left knee
            angle: Left knee angle
    """
    results = {
        "error": None,
        "right": {"error": None, "angle": None},
        "left": {"error": None, "angle": None},
    }

    landmarks = mp_results.pose_landmarks.landmark

    # Calculate right knee angle
    right_hip = [
        landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].x,
        landmarks[mp.solutions.pose.PoseLandmark.RIGHT_HIP.value].y,
    ]
    right_knee = [
        landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].x,
        landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].y,
    ]
    right_ankle = [
        landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].x,
        landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value].y,
    ]
    results["right"]["angle"] = calculate_angle(right_hip, right_knee, right_ankle)

    # Calculate left knee angle
    left_hip = [
        landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].x,
        landmarks[mp.solutions.pose.PoseLandmark.LEFT_HIP.value].y,
    ]
    left_knee = [
        landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].x,
        landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].y,
    ]
    left_ankle = [
        landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].x,
        landmarks[mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value].y,
    ]
    results["left"]["angle"] = calculate_angle(left_hip, left_knee, left_ankle)

    # Draw to image
    if draw_to_image is not None and stage != "down":
        (image, video_dimensions) = draw_to_image

        # Visualize angles
        cv2.putText(
            image,
            str(int(results["right"]["angle"])),
            tuple(np.multiply(right_knee, video_dimensions).astype(int)),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )
        cv2.putText(
            image,
            str(int(results["left"]["angle"])),
            tuple(np.multiply(left_knee, video_dimensions).astype(int)),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )

    if stage != "down":
        return results

    # Evaluation
    results["error"] = False

    if angle_thresholds[0] <= results["right"]["angle"] <= angle_thresholds[1]:
        results["right"]["error"] = False
    else:
        results["right"]["error"] = True
        results["error"] = True

    if angle_thresholds[0] <= results["left"]["angle"] <= angle_thresholds[1]:
        results["left"]["error"] = False
    else:
        results["left"]["error"] = True
        results["error"] = True

    # Draw to image
    if draw_to_image is not None:
        (image, video_dimensions) = draw_to_image

        right_color = (255, 255, 255) if not results["right"]["error"] else (0, 0, 255)
        left_color = (255, 255, 255) if not results["left"]["error"] else (0, 0, 255)

        right_font_scale = 0.5 if not results["right"]["error"] else 1
        left_font_scale = 0.5 if not results["left"]["error"] else 1

        right_thickness = 1 if not results["right"]["error"] else 2
        left_thickness = 1 if not results["left"]["error"] else 2

        # Visualize angles
        cv2.putText(
            image,
            str(int(results["right"]["angle"])),
            tuple(np.multiply(right_knee, video_dimensions).astype(int)),
            cv2.FONT_HERSHEY_COMPLEX,
            right_font_scale,
            right_color,
            right_thickness,
            cv2.LINE_AA,
        )
        cv2.putText(
            image,
            str(int(results["left"]["angle"])),
            tuple(np.multiply(left_knee, video_dimensions).astype(int)),
            cv2.FONT_HERSHEY_COMPLEX,
            left_font_scale,
            left_color,
            left_thickness,
            cv2.LINE_AA,
        )

    return results