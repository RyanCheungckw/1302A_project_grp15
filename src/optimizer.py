def calculate_free_days(schedule_slots):
    """Calculates which days of the week have zero classes."""
    all_days = {"Mon", "Tue", "Wed", "Thu", "Fri"}
    busy_days = {slot["day"] for slot in schedule_slots}
    free_days = all_days - busy_days
    return free_days

def find_best_ge_plan(ge_courses, student_schedule, preferences):
    """
    Evaluates GE courses against student schedule and preferences,
    ranking them by how well they match the requested free days.
    """
    desired_area = preferences.get("desired_area")
    target_free_days = preferences.get("min_free_days", 0)
    
    scored_recommendations = []
    
    for course in ge_courses:
        # Step 1: Filter by GE Area
        if desired_area and course['area'] != desired_area:
            continue
            
        for section in course['sections']:
            # Step 2: Check for time clashes with existing schedule
            has_clash = False
            for student_slot in student_schedule:
                if section['day'] == student_slot['day']:
                    if max(section['start'], student_slot['start']) < min(section['end'], student_slot['end']):
                        has_clash = True
                        break
            
            if has_clash:
                continue  # Skip clashing sections
                
            # Step 3: Simulate combined schedule to count free days
            simulated_schedule = student_schedule + [section]
            free_days = calculate_free_days(simulated_schedule)
            
            # Step 4: Score the plan based on user goals
            score = len(free_days)
            if score >= target_free_days:
                scored_recommendations.append({
                    "code": course["code"],
                    "title": course["title"],
                    "area": course["area"],
                    "section_time": f"{section['day']} {section['start']}-{section['end']}",
                    "free_days_count": score,
                    "free_days_list": list(free_days)
                })
                
    # Sort recommendations by the highest number of free days
    scored_recommendations.sort(key=lambda x: x['free_days_count'], reverse=True)
    return scored_recommendations
