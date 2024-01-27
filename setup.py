from setuptools import setup
import os
from glob import glob


package_name = 'AutoVisionDrive_pkg'


config_module = "AutoVisionDrive_pkg/config"
data_module ="AutoVisionDrive_pkg/data"

detection_module ="AutoVisionDrive_pkg/Detection"
gps_navigation = "AutoVisionDrive_pkg/GPS_Navigation"

det_l_module ="AutoVisionDrive_pkg/Detection/Lanes"
detec_l_a_module="AutoVisionDrive_pkg/Detection/Lanes/a_Segmentation"
detec_l_b_module="AutoVisionDrive_pkg/Detection/Lanes/b_Estimation"
detec_l_c_module="AutoVisionDrive_pkg/Detection/Lanes/c_Cleaning"
detec_l_d_module="AutoVisionDrive_pkg/Detection/Lanes/d_LaneInfo_Extraction"

det_s_module ="AutoVisionDrive_pkg/Detection/Signs"
detec_s_a_module="AutoVisionDrive_pkg/Detection/Signs/Classification"

detec_TL_module="AutoVisionDrive_pkg/Detection/TrafficLights"


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name,detec_l_d_module,detec_l_c_module,detec_l_b_module,detec_l_a_module,det_l_module,detec_s_a_module,det_s_module,detec_TL_module,detection_module,gps_navigation,config_module,data_module],

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        (os.path.join('lib', package_name), glob('scripts/*')),
        (os.path.join('share', package_name,'worlds'), glob('worlds/*')),
            ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aryan',
    maintainer_email='anadipa1@asu.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'spawner_node = AutoVisionDrive_pkg.sdf_spawner:main',
        'computer_vision_node = AutoVisionDrive_pkg.computer_vision_node:main',
        'video_recording_node = AutoVisionDrive_pkg.video_save:main',
        'upper_camera_recording = AutoVisionDrive_pkg.upper_camera_video:main',
        'sdc_V2 = AutoVisionDrive_pkg.sdc_V2:main',
        ],
    },
)
