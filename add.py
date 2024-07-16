from geopy.distance import great_circle, geodesic
from geopy import Point
import numpy as np

def calculate_bearing(pointA, pointB):
    """
    Calculate the bearing between two points.
    """
    lat1 = np.radians(pointA.latitude)
    lat2 = np.radians(pointB.latitude)
    diffLong = np.radians(pointB.longitude - pointA.longitude)

    x = np.sin(diffLong) * np.cos(lat2)
    y = np.cos(lat1) * np.sin(lat2) - (np.sin(lat1) * np.cos(lat2) * np.cos(diffLong))

    initial_bearing = np.arctan2(x, y)

    # Now we have the initial bearing but math.atan2 return values from -180° to +180°
    # so we need to normalize the result to be between 0° and 360°
    initial_bearing = np.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

def add_parallel_points(points,x,y):
    def get_perpendicular_points(lat1, lon1, lat2, lon2, distance):
        point1 = Point(lat1, lon1)
        point2 = Point(lat2, lon2)
        
        bearing = calculate_bearing(point1, point2)
        
        # Calculate the perpendicular bearings
        perp_bearing1 = (bearing + 90) % 360
        perp_bearing2 = (bearing - 90) % 360

        # Calculate the new points at the given distance
        point1_perp = geodesic(kilometers=distance).destination(point1, perp_bearing1)
        point2_perp = geodesic(kilometers=distance).destination(point1, perp_bearing2)
        
        return point1_perp.latitude, point1_perp.longitude, point2_perp.latitude, point2_perp.longitude

    new_points = []
    
    for i in range(len(points) - 1):
        lat1, lon1 = points[i]
        lat2, lon2 = points[i + 1]
        
        perp_lat1, perp_lon1, perp_lat2, perp_lon2 = get_perpendicular_points(lat1, lon1, lat2, lon2, x / 1000.0)
        
        new_points.append((perp_lat1, perp_lon1))
        new_points.append((perp_lat2, perp_lon2))
        
        # Add intermediate points along the perpendicular line
        num_intermediate_points = int(great_circle((perp_lat1, perp_lon1), (perp_lat2, perp_lon2)).meters / y)
        for j in range(1, num_intermediate_points):
            ratio = j / num_intermediate_points
            new_lat = perp_lat1 + ratio * (perp_lat2 - perp_lat1)
            new_lon = perp_lon1 + ratio * (perp_lon2 - perp_lon1)
            new_points.append((new_lat, new_lon))
    
    return new_points


if __name__ == '__main__':
    # Exemplo de uso
    gps_points = [(-19.9253863, -43.9499868), (-19.9242834, -43.9496814), (-19.9218588, -43.9490010)]
    # x = 50  # distância em metros da linha original
    # y = 10  # distância entre os pontos paralelos

    parallel_points = add_parallel_points(gps_points)#, x, y)
    print(parallel_points)
