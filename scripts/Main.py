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


class Coordonnees:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

    def Get_Coordonnes(self, point):
        self.x = point.x
        self.y = point.y
        self.theta = point.theta


class Point(Coordonnees):
    def __init__(self, name, x, y, theta):
        super(Point, self).__init__(x, y, theta)
        self.name = name


class Tools:
    def __init__(self):
        self.nPoint = 20
        self.nbActual_Point = 0
        self.dPointdictionnary = {}
        self.log = logging
        self.data = 0
        self.Code_Aruco = 'None'
        self.Arduino_Order = 0
        self.Arduino_State = 0
        self.Coordonnees = Coordonnees
        self.cgoal = self.Coordonnees(x=0, y=0, theta=0)
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
            self.log.info("you chose the blue side")

    def Next_Point(self):
        if self.nbActual_Point < self.nPoint:
            self.nbActual_Point += 1
            self.log.info('le point actuel est %s', str(self.nbActual_Point))
        else:
            self.log.error('le point actuel est %s et souhaite etre incrementé', str(self.nbActual_Point))
        self.cgoal.Get_Coordonnes(self.dPointdictionnary["Point"+str(self.nbActual_Point)])

    def Logs(self, loglevel):
        self.log.basicConfig(filename='main.log', format='%(asctime)s %(levelname)s:%(message)s', level=loglevel)
        self.log.basicConfig(format='%(levelname)s:%(message)s', level=loglevel)
        self.log.critical('============================ New Try ============================')

    #def Publish(self):
    #    self.publish_order_Arduino = rospy.Publisher('arduinoOrder', Int16, queue_size=10)
    #    self.publish_order_Arduino.publish(self.Arduino_Order)
    #    self.log.info("la valeur %s, a ete publiee dans le topic %s", str(self.Arduino_Order), 'arduinoOrder')
    #    self.publish_goal_point = rospy.Publisher('goal_point', Pose2D, queue_size=10)
    #    self.publish_goal_point.publish(self.goal)
    #    self.log.info("la valeur %s, a ete publiee dans le topic %s", str(self.goal), 'goal_point')
#
#
    #def Subscription(self):
    #    rospy.Subscriber('/arduinoState', Int16, self.Subscrib_Arduino_State)
    #    self.log.debug("la valeur %s, a ete recuperee du topic %s", str(self.Subscrib_Arduino_State), '/arduinoState')
    #    rospy.Subscriber('Code_Aruco', String, self.Subscrib_Code_Aruco)
    #    self.log.debug("la valeur %s, a ete recuperee du topic %s", str(self.Subscrib_Code_Aruco), 'Code_Aruco')
    #    rospy.Subscriber('Arrive', Bool, self.Subscrib_Arrive)
    #    self.log.debug("la valeur %s, a ete recuperee du topic %s", str(self.Subscrib_Arrive), 'Arrive')
    #    rospy.Subscriber('StateClef', Bool, self.bStateClef) # 1 = Debug, 0 = Normal
    #    self.log.debug("la valeur %s, a ete recuperee du topic %s", str(self.bStateClef), 'StateClef')
    #    rospy.Subscriber('StateCote', Bool, self.bStateCote) # 1 = Jaune, 0 = Bleu
    #    self.log.debug("la valeur %s, a ete recuperee du topic %s", str(self.bStateCote), 'StateCote')
    #    rospy.Subscriber('StateTirette', Bool, self.bStateTirette) # 1 = Absente, 0 = Presente
    #    self.log.debug("la valeur %s, a ete recuperee du topic %s", str(self.bStateTirette), 'StateTirette')
#
    #def Subscrib_Arduino_State(self, data):
    #    self.Arduino_State = data
#
    #def Subscrib_Code_Aruco(self, data):
    #    self.Code_Aruco = data
    #
    #def Subscrib_Arrive(self, data):
    #    self.bArrive = data

    def Road_Creation(self):
        self.dPointdictionnary["Point0"] = Point("Point0", 0, 0, 0)
        self.dPointdictionnary["Point1"] = Point("Point1", 1, 0, 0)
        self.dPointdictionnary["Point2"] = Point("Point2", 2, 0, 0)
        self.dPointdictionnary["Point3"] = Point("Point3", 3, 0, 0)
        self.dPointdictionnary["Point4"] = Point("Point4", 4, 0, 0)
        self.dPointdictionnary["Point5"] = Point("Point5", 0, 0, 0)
        self.dPointdictionnary["Point6"] = Point("Point6", 0, 0, 0)
        self.dPointdictionnary["Point7"] = Point("Point7", 0, 0, 0)
        self.dPointdictionnary["Point8"] = Point("Point8", 0, 0, 0)
        self.dPointdictionnary["Point9"] = Point("Point9", 0, 0, 0)
        self.dPointdictionnary["Point10"] = Point("Point10", 0, 0, 0)
        self.dPointdictionnary["Point11"] = Point("Point11", 0, 0, 0)
        self.dPointdictionnary["Point12"] = Point("Point12", 0, 0, 0)
        self.dPointdictionnary["Point13"] = Point("Point13", 0, 0, 0)
        self.dPointdictionnary["Point14"] = Point("Point14", 0, 0, 0)
        if self.Code_Aruco == 'NORD':
            self.log.info('Le Code_Aruco a ete identifie comme etant %s', self.Code_Aruco)
            self.dPointdictionnary["Point15"] = Point("Point15", 0, 0, 0)
            self.dPointdictionnary["Point16"] = Point("Point16", 0, 0, 0)
            self.dPointdictionnary["Point17"] = Point("Point17", 0, 0, 0)
            self.dPointdictionnary["Point18"] = Point("Point18", 0, 0, 0)
            self.dPointdictionnary["Point19"] = Point("Point19", 0, 0, 0)
            self.dPointdictionnary["Point20"] = Point("Point20", 0, 0, 0)
        elif self.Code_Aruco == 'SUD':
            self.log.info('Le Code_Aruco a ete identifie comme etant %s', self.Code_Aruco)
            self.dPointdictionnary["Point15"] = Point("Point15", 0, 0, 0)
            self.dPointdictionnary["Point16"] = Point("Point16", 0, 0, 0)
            self.dPointdictionnary["Point17"] = Point("Point17", 0, 0, 0)
            self.dPointdictionnary["Point18"] = Point("Point18", 0, 0, 0)
            self.dPointdictionnary["Point19"] = Point("Point19", 0, 0, 0)
            self.dPointdictionnary["Point20"] = Point("Point20", 0, 0, 0)
        else:
            self.log.error('Le Code_Aruco n a pas ete identifie, sa valeur = %s', self.Code_Aruco)
            self.dPointdictionnary["Point15"] = Point("Point15", 15, 0, 0)
            self.dPointdictionnary["Point16"] = Point("Point16", 0, 0, 0)
            self.dPointdictionnary["Point17"] = Point("Point17", 0, 0, 0)
            self.dPointdictionnary["Point18"] = Point("Point18", 0, 0, 0)
            self.dPointdictionnary["Point19"] = Point("Point19", 0, 0, 0)
            self.dPointdictionnary["Point20"] = Point("Point20", 20, 0, 0)

        for i in range(0, self.nPoint + 1):
            self.log.debug('le point %s a ete ajoute au dictionnaire : x = %s, y = %s, theta = %s',
                          self.dPointdictionnary["Point"+str(i)].name,
                          str(self.dPointdictionnary["Point"+str(i)].x),
                          str(self.dPointdictionnary["Point"+str(i)].y),
                          str(self.dPointdictionnary["Point"+str(i)].theta)
                          )

def main():

    '''SETUP'''
    tools = Tools()
    tools.Logs(logging.INFO)

    #'''SUBSCRIPTION'''
    #tools.Subscription()
#
    '''PROGRAM'''
    tools.Switch_Side(tools.bStateCote)
    tools.Road_Creation()

    for i in range(0, tools.nPoint+1):
        print(tools.cgoal.x)
        tools.Next_Point()

    #'''PUBLISH'''
    #while not(rospy.is_shutdown()):
#
    #    tools.Publish()
    time.sleep(2)


if __name__ == '__main__':
    #try:
    #    rospy.init_node('Main', anonymous=True)
    #    rospy.Rate(1)
    #    main()
    #    rospy.spin()
    #except rospy.ROSInterruptException:
    #    pass
    main()
