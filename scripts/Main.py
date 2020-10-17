#!/usr/bin/env python
# -*- coding: latin-1 -*-

#import rospy
import time
import math
import logging
#from std_msgs.msg import Int16
#from std_msgs.msg import String
#from std_msgs.msg import Bool
#from geometry_msgs.msg import Pose2D
#from Trajectory.py import Point,main_trajectory


class Tools:
    def __init__(self):
        self.nPoint = 20
        self.dPointdictionnary = {}
        self.log = logging
        self.data = 0
        self.Code_Aruco = ''
        self.Arduino_State = 0
        self.bArrive = False
        self.bStateClef = False
        self.bStateCote = False
        self.bStateTirette = False

    def Switch_Side(self, bBool):
        if bBool:
            self.log.info("you chose the yellow side")
            for i in range(0, self.nPoint):
                self.dPointdictionnary[i][3] = - self.dPointdictionnary[i][3]
                #TODO: conversion des angles
                self.dPointdictionnary[i][4] = self.dPointdictionnary[i][4] + math.pi
        else:
            print("you chose the blue side")

    def Logs(self, loglevel):
        self.log.basicConfig(filename='main.log', format='%(asctime)s %(levelname)s:%(message)s', level=loglevel)
        self.log.basicConfig(format='%(levelname)s:%(message)s', level=loglevel)
        self.log.critical('============================ New Try ============================')

    '''def Publish(self):
        self.publish_order_Arduino = rospy.Publisher('arduinoOrder', Int16, queue_size=10)
        self.publish_goal_point = rospy.Publisher('goal_point', Pose2D,queue_size=10)

    def Subscription(self):
        rospy.Subscriber('/arduinoState', Int16, self.Subscrib_Arduino_State)
        rospy.Subscriber('Code_Aruco', String, self.Subscrib_Code_Aruco)
        rospy.Subscriber('Arrive', BOOL, self.Subscrib_Arrive)
        rospy.Subscriber('StateClef', BOOL, self.bStateClef)
        rospy.Subscriber('StateCote', BOOL, self.bStateCote)
        rospy.Subscriber('StateTirette', BOOL, self.bStateTirette)

    def Subscrib_Arduino_State(self, data):
        self.Arduino_State = data

    def Subscrib_Code_Aruco(self, data):
        self.Code_Aruco = data
    
    def Subscrib_Arrive(self, data):
        self.Arrive = data'''

    def Road_Creation(self):

        self.dPointdictionnary["Point0"] = ("Point0", 0, 0, 0)
        self.dPointdictionnary["Point1"] = ("Point1", 0, 0, 0)
        self.dPointdictionnary["Point2"] = ("Point2", 0, 0, 0)
        self.dPointdictionnary["Point3"] = ("Point3", 0, 0, 0)
        self.dPointdictionnary["Point4"] = ("Point4", 0, 0, 0)
        self.dPointdictionnary["Point5"] = ("Point5", 0, 0, 0)
        self.dPointdictionnary["Point6"] = ("Point6", 0, 0, 0)
        self.dPointdictionnary["Point7"] = ("Point7", 0, 0, 0)
        self.dPointdictionnary["Point8"] = ("Point8", 0, 0, 0)
        self.dPointdictionnary["Point9"] = ("Point9", 0, 0, 0)
        self.dPointdictionnary["Point10"] = ("Point10", 0, 0, 0)
        self.dPointdictionnary["Point11"] = ("Point11", 0, 0, 0)
        self.dPointdictionnary["Point12"] = ("Point12", 0, 0, 0)
        self.dPointdictionnary["Point13"] = ("Point13", 0, 0, 0)
        self.dPointdictionnary["Point14"] = ("Point14", 0, 0, 0)
        if self.Code_Aruco == 'NORD':
            self.log.info('Le Code_Aruco a ete identifie comme etant %s', self.Code_Aruco)
            self.dPointdictionnary["Point15"] = ("Point15", 0, 0, 0)
            self.dPointdictionnary["Point16"] = ("Point16", 0, 0, 0)
            self.dPointdictionnary["Point17"] = ("Point17", 0, 0, 0)
            self.dPointdictionnary["Point18"] = ("Point18", 0, 0, 0)
            self.dPointdictionnary["Point19"] = ("Point19", 0, 0, 0)
            self.dPointdictionnary["Point20"] = ("Point20", 0, 0, 0)
        elif self.Code_Aruco == 'SUD':
            self.log.info('Le Code_Aruco a ete identifie comme etant %s', self.Code_Aruco)
            self.dPointdictionnary["Point15"] = ("Point15", 0, 0, 0)
            self.dPointdictionnary["Point16"] = ("Point16", 0, 0, 0)
            self.dPointdictionnary["Point17"] = ("Point17", 0, 0, 0)
            self.dPointdictionnary["Point18"] = ("Point18", 0, 0, 0)
            self.dPointdictionnary["Point19"] = ("Point19", 0, 0, 0)
            self.dPointdictionnary["Point20"] = ("Point20", 0, 0, 0)
        else:
            self.log.error('Le Code_Aruco n a pas ete identifie, sa valeur = %s', self.Code_Aruco)
            self.dPointdictionnary["Point15"] = ("Point15", 0, 0, 0)
            self.dPointdictionnary["Point16"] = ("Point16", 0, 0, 0)
            self.dPointdictionnary["Point17"] = ("Point17", 0, 0, 0)
            self.dPointdictionnary["Point18"] = ("Point18", 0, 0, 0)
            self.dPointdictionnary["Point19"] = ("Point19", 0, 0, 0)
            self.dPointdictionnary["Point20"] = ("Point20", 0, 0, 0)

        for i in range(0, self.nPoint + 1):
            self.log.info('le point %s a ete ajoute au dictionnaire : x = %s, y = %s, theta = %s',
                          self.dPointdictionnary["Point"+str(i)][1],
                          str(self.dPointdictionnary["Point"+str(i)][2]),
                          str(self.dPointdictionnary["Point"+str(i)][3]),
                          str(self.dPointdictionnary["Point"+str(i)][4])
                          )

def main():
    '''SUBSCRIPTION'''
    # tools.Subscription()

    '''SETUP'''
    tools = Tools()
    tools.Logs(logging.INFO)
    #tools.Switch_Side(bBool)

    '''PROGRAM'''
    tools.Road_Creation()

    '''PUBLISH'''
    #while not(bArrive):
        #tools.Publish()





if __name__ == '__main__':
    main()
