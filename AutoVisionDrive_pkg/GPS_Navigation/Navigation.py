import cv2

from .bot_localization import bot_localizer
from .bot_mapping import bot_mapper
from .bot_pathplanning import bot_pathplanner
from .bot_motionplanning import bot_motionplanner

# importing utility functions for taking destination from user
from .utilities import Debugging,click_event,find_point_in_FOR
import sys
from . import config
# functionality to provide on device prompt to user to select destination
from .utilities import disp_on_mydev
# motionplanning (Visualization) Imports
from .utilities_disp import disp_SatNav
class Navigator():

    def __init__(self):
        
        # Creating objects for each stage of the robot navigation
        self.bot_localizer = bot_localizer()
        self.bot_mapper = bot_mapper()
        self.bot_pathplanner = bot_pathplanner()
        self.bot_motionplanner = bot_motionplanner()

        self.debugging = Debugging()

        
        self.accquiring_destination = True
        
        self.destination = []

        
        self.device_view = []
        
        self.screen_x = 0
        self.screen_y = 0



    
    def navigate_to_home(self,sat_view,bot_view):
            
        self.debugging.setDebugParameters()

               
        frame_disp = sat_view.copy()
        
               
        self.bot_localizer.localize_bot(sat_view, frame_disp)

        
        if self.accquiring_destination:
            
            self.device_view,self.screen_x,self.screen_y = disp_on_mydev(sat_view)
            cv2.namedWindow("Mark your destination!!!",cv2.WINDOW_NORMAL)
            cv2.imshow("Mark your destination!!!",self.device_view)
            cv2.setMouseCallback("Mark your destination!!!", click_event)
            while(self.destination==[]):
                self.destination = config.destination
                cv2.waitKey(1)
            
            if self.destination!=[]:
                self.destination = (self.destination[0]-self.screen_x,self.destination[1]-self.screen_y)
                
                cv2.destroyWindow("Mark your destination!!!")
                self.accquiring_destination = False
                
                self.destination = find_point_in_FOR(self.destination,self.bot_localizer.transform_arr,self.bot_localizer.rot_mat,sat_view.shape[1],sat_view.shape[0])
                cv2.namedWindow("SatView (Live)",cv2.WINDOW_NORMAL)
            else:
                print("Destination not specified.... Exiting!!!")
                sys.exit()

 
        self.bot_mapper.graphify(self.bot_localizer.maze_og,self.bot_localizer.loc_car,self.destination,self.bot_localizer.car_rect)

        
        start = self.bot_mapper.Graph.start
        end = self.bot_mapper.Graph.end
        maze = self.bot_mapper.maze

        self.bot_pathplanner.find_path_nd_display(self.bot_mapper.Graph.graph, start, end, maze,method="dijisktra")
        self.bot_pathplanner.find_path_nd_display(self.bot_mapper.Graph.graph, start, end, maze,method="a_star")
        if config.debug and config.debug_pathplanning:
            print("\nNodes Visited [Dijisktra V A-Star*] = [ {} V {} ]".format(self.bot_pathplanner.dijisktra.dijiktra_nodes_visited,self.bot_pathplanner.astar.astar_nodes_visited))



        bot_loc = self.bot_localizer.loc_car
        path = self.bot_pathplanner.path_to_goal

        bot_loc_wrt_rdntwork = self.bot_localizer.loc_car_wrt_rdntwork

        self.bot_motionplanner.nav_path(bot_loc, bot_loc_wrt_rdntwork, path)

        img_shortest_path = self.bot_pathplanner.img_shortest_path
        self.bot_motionplanner.display_control_mechanism_in_action(bot_loc, path, img_shortest_path, self.bot_localizer, frame_disp)

        curr_speed = self.bot_motionplanner.actual_speed
        curr_angle = self.bot_motionplanner.actual_angle
        maze_IntrstPts = self.bot_mapper.maze_interestPts
        choosen_route = self.bot_pathplanner.choosen_route
        transform_arr = self.bot_localizer.transform_arr        
        crp_amt = self.bot_mapper.crp_amt
        disp_SatNav(frame_disp,bot_view,curr_speed,curr_angle,maze_IntrstPts,choosen_route,img_shortest_path,transform_arr,crp_amt)


        self.device_view[self.screen_y:frame_disp.shape[0]+self.screen_y,self.screen_x:frame_disp.shape[1]+self.screen_x] = frame_disp
        cv2.imshow("SatView (Live)", self.device_view)
        cv2.waitKey(1)

