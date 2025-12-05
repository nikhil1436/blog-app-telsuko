from datetime import datetime, timedelta

def generate_slots(working_start, working_end, booked, duration):
    slots = []

    current = datetime.combine(datetime.today(), working_start)
    end = datetime.combine(datetime.today(), working_end)

    booked_times = [
        (datetime.combine(datetime.today(), b.start_time),
         datetime.combine(datetime.today(), b.end_time))
        for b in booked
    ]

    while current + timedelta(minutes=duration) <= end:
        slot_start = current
        slot_end = current + timedelta(minutes=duration)

        # overlap check
        overlap = False
        for b_start, b_end in booked_times:
            if not (slot_end <= b_start or slot_start >= b_end):
                overlap = True
                break

        if not overlap:
            slots.append({
                "start": slot_start.time().strftime("%H:%M"),
                "end": slot_end.time().strftime("%H:%M")
            })

        current += timedelta(minutes=duration)

    return slots
