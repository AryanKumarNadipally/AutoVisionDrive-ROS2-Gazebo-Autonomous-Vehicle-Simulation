from ...config import config

from .a_Segmentation.colour_segmentation_final import Segment_Colour

from .b_Estimation.Our_EstimationAlgo import Estimate_MidLane

from .c_Cleaning.CheckifYellowLaneCorrect_RetInnerBoundary import GetYellowInnerEdge
from .c_Cleaning.ExtendLanesAndRefineMidLaneEdge import ExtendShortLane

from .d_LaneInfo_Extraction.GetStateInfoandDisplayLane import FetchInfoAndDisplay



def detect_Lane(img):
        
        img_cropped = img[config.CropHeight_resized:,:]

        
        Mid_edge_ROI,Mid_ROI_mask,Outer_edge_ROI,OuterLane_TwoSide,OuterLane_Points = Segment_Colour(img_cropped,config.minArea_resized)
       
        
        Estimated_midlane = Estimate_MidLane(Mid_edge_ROI,config.MaxDist_resized)

        
        OuterLane_OneSide,Outer_cnts_oneSide,Mid_cnts,Offset_correction = GetYellowInnerEdge(OuterLane_TwoSide,Estimated_midlane,OuterLane_Points)#3ms
        
        Estimated_midlane,OuterLane_OneSide = ExtendShortLane(Estimated_midlane,Mid_cnts,Outer_cnts_oneSide,OuterLane_OneSide)
        
        
        Distance , Curvature = FetchInfoAndDisplay(Mid_edge_ROI,Estimated_midlane,OuterLane_OneSide,img_cropped,Offset_correction)

        return Distance,Curvature
       