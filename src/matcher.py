def check_time_clash(ge_slot, student_schedule):
    """Returns True if there is a time conflict, False otherwise."""
    for item in student_schedule:
        if ge_slot['day'] == item['day']:
            # Overlap condition: max(start1, start2) < min(end1, end2)
            if max(ge_slot['start'], item['start']) < min(ge_slot['end'], item['end']):
                return True
    return False

def find_clash_free_courses(ge_courses_with_slots, student_schedule):
    available_courses = []
    for course in ge_courses_with_slots:
        has_clash = any(check_time_clash(slot, student_schedule) for slot in course['slots'])
        if not has_clash:
            available_courses.append(course)
    return available_courses
