from datetime import datetime, timedelta
import math

def solution(fees, records):
    answer = []
    a, b, c, d = fees

    def calculate_parking_time(parking_log):
        parking_times = {}
        vehicle_status = {}

        for entry in parking_log:
            time_str, vehicle_num, status = entry.split()
            current_time = datetime.strptime(time_str, "%H:%M")

            if status == "IN":
                vehicle_status[vehicle_num] = current_time
            elif status == "OUT":
                if vehicle_num in vehicle_status:
                    in_time = vehicle_status[vehicle_num]
                    parking_duration = (current_time - in_time).total_seconds() / 60
                    parking_times[vehicle_num] = parking_times.get(vehicle_num, 0) + parking_duration
                    del vehicle_status[vehicle_num]

        
        end_of_day = datetime.strptime("23:59", "%H:%M")
        for vehicle_num, in_time in vehicle_status.items():
            parking_duration = (end_of_day - in_time).total_seconds() / 60
            parking_times[vehicle_num] = parking_times.get(vehicle_num, 0) + parking_duration

        return parking_times
    
    
    result = calculate_parking_time(records)
    sorted_result = sorted(result.items())
    
    
    
    for i in sorted_result:
        e, f = i
        if f <= a:
            answer.append(b)
        else:
            answer.append(b + (math.ceil((f - a) / c) * d))
            # answer.append(b + (round(((f - a) / c) + 0.5) * d))
        
    return answer