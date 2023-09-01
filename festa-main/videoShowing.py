import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import pickle 
import traceback 
import math

from calculateForVideo import *
from classOfExercises import *

def video_showing(workOutType):
    if workOutType == "lunge":
        lunge()
    elif workOutType == "plank":
        plank()
    elif workOutType == "squat":
        squat()
    else:
        raise Exception("Not yet implemented")
def lunge():
    HEADERS = ['label', 'nose_x', 'nose_y', 'nose_z', 'nose_v', 'left_shoulder_x', 'left_shoulder_y', 'left_shoulder_z', 'left_shoulder_v', 'right_shoulder_x', 'right_shoulder_y', 'right_shoulder_z', 'right_shoulder_v', 'left_hip_x', 'left_hip_y', 'left_hip_z', 'left_hip_v', 'right_hip_x', 'right_hip_y', 'right_hip_z', 'right_hip_v', 'left_knee_x', 'left_knee_y', 'left_knee_z', 'left_knee_v', 'right_knee_x', 'right_knee_y', 'right_knee_z', 'right_knee_v', 'left_ankle_x', 'left_ankle_y', 'left_ankle_z', 'left_ankle_v', 'right_ankle_x', 'right_ankle_y', 'right_ankle_z', 'right_ankle_v', 'left_heel_x', 'left_heel_y', 'left_heel_z', 'left_heel_v', 'right_heel_x', 'right_heel_y', 'right_heel_z', 'right_heel_v', 'left_foot_index_x', 'left_foot_index_y', 'left_foot_index_z', 'left_foot_index_v', 'right_foot_index_x', 'right_foot_index_y', 'right_foot_index_z', 'right_foot_index_v'] # Label column
    with open("./models/lunge_counter.pkl", "rb") as f: lunge_counter = pickle.load(f)
    with open("./models/lunge_errorDetection.pkl", "rb") as f: lunge_errorDetection = pickle.load(f)
    with open("./models/lunge_input_scaler.pkl", "rb") as f: lunge_input_scaler = pickle.load(f)

    cap = cv2.VideoCapture(0)
    cap.set(3, 8000)  # width
    cap.set(4, 4800)  # height
    current_stage = ""
    counter = 0

    prediction_probability_threshold = 0.8
    ANGLE_THRESHOLDS = [60, 135]

    knee_over_toe = False

    with mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, image = cap.read()

            if not ret:
                break

            # Reduce size of a frame
            image = rescale_frame(image, 50)
            video_dimensions = [image.shape[1], image.shape[0]]

            # Recolor image from BGR to RGB for mediapipe
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            if not results.pose_landmarks:
                print("No human found")
                continue

            # Recolor image from BGR to RGB for mediapipe
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw landmarks and connections
            mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS, mp.solutions.drawing_utils.DrawingSpec(color=(244, 117, 66), thickness=2, circle_radius=2), mp.solutions.drawing_utils.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=1))

            # Make detection
            try:
                tmp = [
                    "NOSE",
                    "LEFT_SHOULDER",
                    "RIGHT_SHOULDER",
                    "LEFT_HIP",
                    "RIGHT_HIP",
                    "LEFT_KNEE",
                    "RIGHT_KNEE",
                    "LEFT_ANKLE",
                    "RIGHT_ANKLE",
                    "LEFT_HEEL",
                    "RIGHT_HEEL",
                    "LEFT_FOOT_INDEX",
                    "RIGHT_FOOT_INDEX",
                ]
                # Extract keypoints from frame for the input
                row = extract_important_keypoints(results,  tmp)
                X = pd.DataFrame([row], columns=HEADERS[1:])
                X = pd.DataFrame(lunge_input_scaler.transform(X))

                # Make prediction and its probability
                stage_predicted_class = lunge_counter.predict(X)[0]
                stage_prediction_probabilities = lunge_counter.predict_proba(X)[0]
                stage_prediction_probability = round(stage_prediction_probabilities[stage_prediction_probabilities.argmax()], 2)

                # Evaluate model prediction
                if stage_predicted_class == "I" and stage_prediction_probability >= prediction_probability_threshold:
                    current_stage = "init"
                elif stage_predicted_class == "M" and stage_prediction_probability >= prediction_probability_threshold: 
                    current_stage = "mid"
                elif stage_predicted_class == "D" and stage_prediction_probability >= prediction_probability_threshold:
                    if current_stage in ["mid", "init"]:
                        counter += 1
                    
                    current_stage = "down"
                
                # Error detection
                # Knee angle
                analyze_knee_angle(mp_results=results, stage=current_stage, angle_thresholds=ANGLE_THRESHOLDS, draw_to_image=(image, video_dimensions))

                # Knee over toe
                err_predicted_class = err_prediction_probabilities = err_prediction_probability = None
                if current_stage == "down":
                    err_predicted_class = lunge_errorDetection.predict(X)[0]
                    err_prediction_probabilities = lunge_errorDetection.predict_proba(X)[0]
                    err_prediction_probability = round(err_prediction_probabilities[err_prediction_probabilities.argmax()], 2)
                    
                
                # Visualization
                # Status box
                cv2.rectangle(image, (0, 0), (800, 45), (245, 117, 16), -1)

                # Display stage prediction
                cv2.putText(image, "STAGE", (15, 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(stage_prediction_probability), (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(image, current_stage, (50, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

                # Display error prediction
                cv2.putText(image, "K_O_T", (200, 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(err_prediction_probability), (195, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(image, str(err_predicted_class), (245, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

                # Display Counter
                cv2.putText(image, "COUNTER", (110, 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(counter), (110, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

            except Exception as e:
                print(f"Error: {e}")
                traceback.print_exc()
                break
            
            cv2.imshow("CV2", image)
            
            # Press Q to close cv2 window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

def plank():
    mp.solutions.drawing_utils = mp.solutions.drawing_utils
    mp.solutions.pose = mp.solutions.pose
    # Determine important landmarks for plank
    IMPORTANT_LMS = [
        "NOSE",
        "LEFT_SHOULDER",
        "RIGHT_SHOULDER",
        "LEFT_ELBOW",
        "RIGHT_ELBOW",
        "LEFT_WRIST",
        "RIGHT_WRIST",
        "LEFT_HIP",
        "RIGHT_HIP",
        "LEFT_KNEE",
        "RIGHT_KNEE",
        "LEFT_ANKLE",
        "RIGHT_ANKLE",
        "LEFT_HEEL",
        "RIGHT_HEEL",
        "LEFT_FOOT_INDEX",
        "RIGHT_FOOT_INDEX",
    ]

    # Generate all columns of the data frame

    HEADERS = ["label"] # Label column

    for lm in IMPORTANT_LMS: HEADERS += [f"{lm.lower()}_x", f"{lm.lower()}_y", f"{lm.lower()}_z", f"{lm.lower()}_v"]

    # Load model
    with open("./models/plank.pkl", "rb") as f:
        sklearn_model = pickle.load(f)

    # Dump input scaler
    with open("./models/plank_input_scaler.pkl", "rb") as f2:
        input_scaler = pickle.load(f2)

    cap = cv2.VideoCapture(0)
    current_stage = ""
    prediction_probability_threshold = 0.6

    with mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, image = cap.read()

            if not ret:
                break

            # Reduce size of a frame
            image = rescale_frame(image, 50)
            # image = cv2.flip(image, 1)

            # Recolor image from BGR to RGB for mediapipe
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            if not results.pose_landmarks:
                print("No human found")
                continue

            # Recolor image from BGR to RGB for mediapipe
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw landmarks and connections
            mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS, mp.solutions.drawing_utils.DrawingSpec(color=(244, 117, 66), thickness=2, circle_radius=2), mp.solutions.drawing_utils.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=1))

            # Make detection
            try:
                # Extract keypoints from frame for the input
                row = extract_important_keypoints(results, IMPORTANT_LMS)
                X = pd.DataFrame([row], columns=HEADERS[1:])
                X = pd.DataFrame(input_scaler.transform(X))

                # Make prediction and its probability
                predicted_class = sklearn_model.predict(X)[0]
                prediction_probability = sklearn_model.predict_proba(X)[0]
                #print(predicted_class, prediction_probability)

                # Evaluate model prediction
                if predicted_class == 0 and prediction_probability[prediction_probability.argmax()] >= prediction_probability_threshold:
                    current_stage = "Correct"
                elif predicted_class == 2 and prediction_probability[prediction_probability.argmax()] >= prediction_probability_threshold: 
                    current_stage = "Low back"
                elif predicted_class == 1 and prediction_probability[prediction_probability.argmax()] >= prediction_probability_threshold: 
                    current_stage = "High back"
                else:
                    current_stage = "unk"
                
                # Visualization
                # Status box
                cv2.rectangle(image, (0, 0), (250, 60), (245, 117, 16), -1)

                # Display class
                cv2.putText(image, "CLASS", (95, 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, current_stage, (90, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                # Display probability
                cv2.putText(image, "PROB", (15, 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(round(prediction_probability[np.argmax(prediction_probability)], 2)), (10, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            except Exception as e:
                print(f"Error: {e}")
            
            cv2.imshow("CV2", image)
            
            # Press Q to close cv2 window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

def squat():
    IMPORTANT_LMS = [
        "NOSE",
        "LEFT_SHOULDER",
        "RIGHT_SHOULDER",
        "LEFT_HIP",
        "RIGHT_HIP",
        "LEFT_KNEE",
        "RIGHT_KNEE",
        "LEFT_ANKLE",
        "RIGHT_ANKLE"
    ]

    headers = ["label"] # Label column

    for lm in IMPORTANT_LMS:
        headers += [f"{lm.lower()}_x", f"{lm.lower()}_y", f"{lm.lower()}_z", f"{lm.lower()}_v"]
    with open("./models/squat_counter.pkl", "rb") as f: count_model = pickle.load(f)
    cap = cv2.VideoCapture(0)

    # Counter vars
    counter = 0
    current_stage = ""
    PREDICTION_PROB_THRESHOLD = 0.7

    # Error vars
    VISIBILITY_THRESHOLD = 0.6
    FOOT_SHOULDER_RATIO_THRESHOLDS = [1.2, 2.8]
    KNEE_FOOT_RATIO_THRESHOLDS = {
        "up": [0.5, 1.0],
        "middle": [0.7, 1.0],
        "down": [0.7, 1.1],
    }


    with mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, image = cap.read()

            if not ret:
                break
            
            # Reduce size of a frame
            image = rescale_frame(image, 100)

            # Recolor image from BGR to RGB for mediapipe
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)
            if not results.pose_landmarks:
                continue

            # Recolor image from BGR to RGB for mediapipe
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw landmarks and connections
            mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS, mp.solutions.drawing_utils.DrawingSpec(color=(244, 117, 66), thickness=2, circle_radius=2), mp.solutions.drawing_utils.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=1))

            # Make detection
            try:
                # * Model prediction for SQUAT counter
                # Extract keypoints from frame for the input
                row = extract_important_keypoints(results, IMPORTANT_LMS)
                X = pd.DataFrame([row])
                # Make prediction and its probability
                predicted_class = count_model.predict(X)[0]
                prediction_probabilities = count_model.predict_proba(X)[0]
                prediction_probability = round(prediction_probabilities[prediction_probabilities.argmax()], 2)

                # Evaluate model prediction
                if predicted_class == "down" and prediction_probability >= PREDICTION_PROB_THRESHOLD:
                    current_stage = "down"
                elif current_stage == "down" and predicted_class == "up" and prediction_probability >= PREDICTION_PROB_THRESHOLD: 
                    current_stage = "up"
                    counter += 1

                # Analyze squat pose
                analyzed_results = analyze_foot_knee_placement(results=results, stage=current_stage, foot_shoulder_ratio_thresholds=FOOT_SHOULDER_RATIO_THRESHOLDS, knee_foot_ratio_thresholds=KNEE_FOOT_RATIO_THRESHOLDS, visibility_threshold=VISIBILITY_THRESHOLD)

                foot_placement_evaluation = analyzed_results["foot_placement"]
                knee_placement_evaluation = analyzed_results["knee_placement"]
                
                # * Evaluate FOOT PLACEMENT error
                if foot_placement_evaluation == -1:
                    foot_placement = "UNK"
                elif foot_placement_evaluation == 0:
                    foot_placement = "Correct"
                elif foot_placement_evaluation == 1:
                    foot_placement = "Too tight"
                elif foot_placement_evaluation == 2:
                    foot_placement = "Too wide"
                
                # * Evaluate KNEE PLACEMENT error
                if knee_placement_evaluation == -1:
                    knee_placement = "UNK"
                elif knee_placement_evaluation == 0:
                    knee_placement = "Correct"
                elif knee_placement_evaluation == 1:
                    knee_placement = "Too tight"
                elif knee_placement_evaluation == 2:
                    knee_placement = "Too wide"
                
                # Visualization
                # Status box
                cv2.rectangle(image, (0, 0), (500, 60), (245, 117, 16), -1)

                # Display class
                #print(predicted_class, prediction_probability)
                cv2.putText(image, "COUNT", (10, 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, f'{str(counter)}, {"down" if predicted_class == 0 else "up"}, {str(prediction_probability)}', (5, 40), cv2.FONT_HERSHEY_COMPLEX, .7, (255, 255, 255), 2, cv2.LINE_AA)

                # Display Foot and Shoulder width ratio
                cv2.putText(image, "FOOT", (200, 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, foot_placement, (195, 40), cv2.FONT_HERSHEY_COMPLEX, .7, (255, 255, 255), 2, cv2.LINE_AA)

                # Display knee and Shoulder width ratio
                cv2.putText(image, "KNEE", (330, 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, knee_placement, (325, 40), cv2.FONT_HERSHEY_COMPLEX, .7, (255, 255, 255), 2, cv2.LINE_AA)

            except Exception as e:
                print(f"Error: {e}")
            
            cv2.imshow("CV2", image)
            
            # Press Q to close cv2 window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

def calculate_distance(pointX, pointY) -> float:
    '''
    Calculate a distance between 2 points
    '''

    x1, y1 = pointX
    x2, y2 = pointY

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def analyze_foot_knee_placement(results, stage: str, foot_shoulder_ratio_thresholds: list, knee_foot_ratio_thresholds: dict, visibility_threshold: int) -> dict:
    '''
    Calculate the ratio between the foot and shoulder for FOOT PLACEMENT analysis
    
    Calculate the ratio between the knee and foot for KNEE PLACEMENT analysis

    Return result explanation:
        -1: Unknown result due to poor visibility
        0: Correct knee placement
        1: Placement too tight
        2: Placement too wide
    '''
    analyzed_results = {
        "foot_placement": -1,
        "knee_placement": -1,
    }

    landmarks = results.pose_landmarks.landmark

    # * Visibility check of important landmarks for foot placement analysis
    left_foot_index_vis = landmarks[mp.solutions.pose.PoseLandmark.LEFT_FOOT_INDEX.value].visibility
    right_foot_index_vis = landmarks[mp.solutions.pose.PoseLandmark.RIGHT_FOOT_INDEX.value].visibility

    left_knee_vis = landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].visibility
    right_knee_vis = landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].visibility

    # If visibility of any keypoints is low cancel the analysis
    if (left_foot_index_vis < visibility_threshold or right_foot_index_vis < visibility_threshold or left_knee_vis < visibility_threshold or right_knee_vis < visibility_threshold):
        return analyzed_results
    
    # * Calculate shoulder width
    left_shoulder = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value].y]
    right_shoulder = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    shoulder_width = calculate_distance(left_shoulder, right_shoulder)

    # * Calculate 2-foot width
    left_foot_index = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_FOOT_INDEX.value].x, landmarks[mp.solutions.pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
    right_foot_index = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x, landmarks[mp.solutions.pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]
    foot_width = calculate_distance(left_foot_index, right_foot_index)

    # * Calculate foot and shoulder ratio
    foot_shoulder_ratio = round(foot_width / shoulder_width, 1)

    # * Analyze FOOT PLACEMENT
    min_ratio_foot_shoulder, max_ratio_foot_shoulder = foot_shoulder_ratio_thresholds
    if min_ratio_foot_shoulder <= foot_shoulder_ratio <= max_ratio_foot_shoulder:
        analyzed_results["foot_placement"] = 0
    elif foot_shoulder_ratio < min_ratio_foot_shoulder:
        analyzed_results["foot_placement"] = 1
    elif foot_shoulder_ratio > max_ratio_foot_shoulder:
        analyzed_results["foot_placement"] = 2
    
    # * Visibility check of important landmarks for knee placement analysis
    left_knee_vis = landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].visibility
    right_knee_vis = landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].visibility

    # If visibility of any keypoints is low cancel the analysis
    if (left_knee_vis < visibility_threshold or right_knee_vis < visibility_threshold):
        print("Cannot see foot")
        return analyzed_results

    # * Calculate 2 knee width
    left_knee = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp.solutions.pose.PoseLandmark.LEFT_KNEE.value].y]
    right_knee = [landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value].y]
    knee_width = calculate_distance(left_knee, right_knee)

    # * Calculate foot and shoulder ratio
    knee_foot_ratio = round(knee_width / foot_width, 1)

    # * Analyze KNEE placement
    up_min_ratio_knee_foot, up_max_ratio_knee_foot = knee_foot_ratio_thresholds.get("up")
    middle_min_ratio_knee_foot, middle_max_ratio_knee_foot = knee_foot_ratio_thresholds.get("middle")
    down_min_ratio_knee_foot, down_max_ratio_knee_foot = knee_foot_ratio_thresholds.get("down")

    if stage == "up":
        if up_min_ratio_knee_foot <= knee_foot_ratio <= up_max_ratio_knee_foot:
            analyzed_results["knee_placement"] = 0
        elif knee_foot_ratio < up_min_ratio_knee_foot:
            analyzed_results["knee_placement"] = 1
        elif knee_foot_ratio > up_max_ratio_knee_foot:
            analyzed_results["knee_placement"] = 2
    elif stage == "middle":
        if middle_min_ratio_knee_foot <= knee_foot_ratio <= middle_max_ratio_knee_foot:
            analyzed_results["knee_placement"] = 0
        elif knee_foot_ratio < middle_min_ratio_knee_foot:
            analyzed_results["knee_placement"] = 1
        elif knee_foot_ratio > middle_max_ratio_knee_foot:
            analyzed_results["knee_placement"] = 2
    elif stage == "down":
        if down_min_ratio_knee_foot <= knee_foot_ratio <= down_max_ratio_knee_foot:
            analyzed_results["knee_placement"] = 0
        elif knee_foot_ratio < down_min_ratio_knee_foot:
            analyzed_results["knee_placement"] = 1
        elif knee_foot_ratio > down_max_ratio_knee_foot:
            analyzed_results["knee_placement"] = 2
    
    return analyzed_results