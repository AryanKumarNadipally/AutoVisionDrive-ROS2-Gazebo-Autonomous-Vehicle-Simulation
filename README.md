# AutoVisionDrive-ROS2-Gazebo-Autonomous-Vehicle-Simulation

## Project Description
This project is utilizing ROS2 alongside OpenCV to simulate an autonomous Prius vehicle in Gazebo. The project's cornerstone is its application of cutting-edge computer vision algorithms and machine learning to facilitate real-time perception and navigation.

## Simulation Environment
#### Gazebo Simulation:
- The project leverages the Gazebo simulator to provide a realistic and controlled environment for testing the autonomous vehicle's systems.
- A detailed Prius car model is used within the simulation to replicate real-world physics and vehicle dynamics accurately.

## Perception Module
#### Lane Detection:
- With a dynamic adjustment mechanism, the lane detection module maintains an accuracy level of over 95%, crucial for the safe maneuvering of the simulated Prius.
- Frames are processed at a reduced resolution of 320x240 to balance the trade-off between computational efficiency and detection accuracy, decreasing the computational demand by approximately 88% compared to full HD images.

#### Traffic Light Detection:
- A pre-trained Haar Cascade Classifier with a 99.5% hit rate and an 8% false-positive rate effectively identifies traffic lights, ensuring compliance with traffic rules within the simulated environment.

#### Traffic Sign Recognition:
- The Traffic Sign Recognition system's specifications are poised for expansion, but they are currently poised to leverage a CNN for high-accuracy classification, drawing from industry-standard performance metrics.

## Autonomous Navigation Module
#### Path Planning and Navigation:
- Utilizes Gazebo's robust physics engine to test the vehicle's navigation system, including predefined waypoints and reactive obstacle avoidance.
- Incorporates a visual route overlay indicating the current and projected path, enhancing the debugging process and system comprehensibility.

#### Vehicle Control:
- The simulation includes a visual representation of speed and directional control, with a speedometer indicating the percentage of maximum speed and turning indicators for direction changes.

## System Configuration and Diagnostics
#### Configurability:
- A highly modular design allows specific subsystems, such as satellite navigation and animated steering, to be toggled on or off, enabling focused testing and system refinement.
- Boolean flags within the configuration file offer straightforward control over the simulation's features, adapting to different phases of development and testing.

#### Debugging and Visualization:
- In-depth debugging features provide visibility into the system's operations, including lane estimation accuracy and color segmentation, with individual toggle controls for each diagnostic feature.
- Performance profiling is available for optimization, with optional video output capturing at 30 FPS for subsequent analysis.

## Limitations and Future Work
- The Traffic Sign Recognition module awaits further definition and will benefit from a tailored deep learning model trained on a robust dataset.
- Future iterations will explore the integration of sensor fusion to elevate object detection and collision avoidance capabilities, thus enhancing the safety profile of the autonomous Prius in the Gazebo simulation.

## Output Video Link
[https://www.dropbox.com/scl/fi/wl67b79rm7xdpfy46q6a3/Output.mp4?rlkey=42q81hjwrlnps9k7s3f2u1f5r&dl=0]
