#!/usr/bin/env python

import rospy
import actionlib
from course_web_dev_ros.msg import WaypointActionFeedback, WaypointActionResult, WaypointActionAction, WaypointActionGoal

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
        # Enviar varias metas (puedes modificar estas coordenadas según sea necesario)
        # send_goal(0.6755 , -0.48, 0.0)
        send_goal(0.7037 ,  0.4217, 0.0)

        # Puedes enviar más metas llamando a send_goal con diferentes coordenadas
    except rospy.ROSInterruptException:
        rospy.logerr("Interrupción del programa")
