#!/usr/bin/env python

import rospy
import actionlib
from course_web_dev_ros.msg import WaypointActionFeedback, WaypointActionResult, WaypointActionAction, WaypointActionGoal
from geometry_msgs.msg import Twist, Point
import time

def send_goal(x, y, z):
    # Inicializar el nodo
    rospy.init_node('waypoint_client')

    # Crear un cliente de acción
    client = actionlib.SimpleActionClient('/tortoisebot_as', WaypointActionAction)

    # Esperar a que el servidor de acción esté disponible
    rospy.loginfo("Esperando al servidor de acción...")
    client.wait_for_server()

    # Crear un mensaje de objetivo
    goal = WaypointActionGoal()
    goal.position.x = x
    goal.position.y = y
    goal.position.z = z

    # Enviar el objetivo al servidor de acción
    rospy.loginfo("Enviando meta: %s", goal)
    client.send_goal(goal)

    # Esperar la finalización de la acción
    rospy.loginfo("Esperando el resultado...")
    client.wait_for_result()

    # Obtener el resultado
    result = client.get_result()
    rospy.loginfo("Resultado: %s", result)

if __name__ == '__main__':
    try:
        
        point_1 = Point()
        point_1.x = 0.67 
        point_1.y = -0.49

        point_2 = Point()
        point_2.x = 0.70
        point_2.y = 0.42

        #?
        point_3 = Point()
        point_3.x = 0.283
        point_3.y = 0.416

        point_4 = Point()
        point_4.x = 0.232
        point_4.y = 0.055

        point_5 = Point()
        point_5.x = -0.10
        point_5.y = -0.00
    
        #Left behind start line
        point_7 = Point()
        point_7.x = -0.20
        point_7.y = -0.55

        point_8 = Point() 
        point_8.x = -0.60
        point_8.y = -0.49


        #Right side
        point_9 = Point()
        point_9.x = -0.20
        point_9.y = 0.55

        point_10 = Point()
        point_10.x = -0.5956
        point_10.y =  0.4430

        # Enviar varias metas (puedes modificar estas coordenadas según sea necesario)
        send_goal(point_1.x , point_1.y, 0.0)
        time.sleep(1)
        send_goal(point_2.x ,  point_2.y, 0.0)
        time.sleep(1)
        send_goal(point_3.x ,  point_3.y, 0.0)
        time.sleep(1)
        send_goal(point_4.x ,  point_4.y, 0.0)
        time.sleep(1)
        send_goal(point_5.x ,  point_5.y, 0.0)
        time.sleep(1)
        send_goal(point_7.x ,  point_7.y, 0.0)
        time.sleep(1)
        send_goal(point_8.x ,  point_8.y, 0.0)
        time.sleep(1)
        send_goal(point_7.x ,  point_7.y, 0.0)
        time.sleep(1)
        send_goal(point_5.x ,  point_5.y, 0.0)
        time.sleep(1)
        send_goal(point_9.x ,  point_9.y, 0.0)
        time.sleep(1)
        send_goal(point_10.x ,  point_10.y, 0.0)
        time.sleep(1)
        # Puedes enviar más metas llamando a send_goal con diferentes coordenadas
    except rospy.ROSInterruptException:
        rospy.logerr("Interrupción del programa")
