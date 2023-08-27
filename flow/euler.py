import numpy as np
import cv2

def amplify_motion_phase_based(input_video, amplification_factor, output_video):
    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        print("Error opening video file")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

    ret, prev_frame = cap.read()
    prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    
    while True:
        ret, curr_frame = cap.read()
        if not ret:
            break

        curr_frame_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

        # Calculate optical flow
        flow = cv2.calcOpticalFlowFarneback(prev_frame, curr_frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # Calculate phase shift
        phase_shift = np.arctan2(flow[..., 1], flow[..., 0])

        # Amplify phase
        amplified_phase = phase_shift * amplification_factor

        # Calculate amplified optical flow
        amplified_flow = np.stack((np.cos(amplified_phase), np.sin(amplified_phase)), axis=-1)

        # Apply amplified flow to create new frame
        new_frame = cv2.remap(curr_frame, amplified_flow, None, cv2.INTER_LINEAR)

        # Write the new frame to the output video
        out.write(new_frame)

        prev_frame = curr_frame_gray

    cap.release()
    out.release()

# Example usage
input_video = './input_video.mp4'
output_video = 'output_video_amplified.avi'
amplification_factor = 10

amplify_motion_phase_based(input_video, amplification_factor, output_video)
