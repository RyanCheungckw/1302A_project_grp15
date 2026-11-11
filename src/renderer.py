from tabulate import tabulate

def render_weekly_timetable(student_schedule, selected_ge_section=None):
    """Renders a text-based weekly timetable grid."""
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    time_slots = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    
    # Initialize empty grid
    grid = {time: {day: "" for day in days} for time in time_slots}
    
    # Populate existing schedule
    all_classes = student_schedule + ([selected_ge_section] if selected_ge_section else [])
    for cls in all_classes:
        day = cls.get("day")
        start_hour = cls.get("start")[:2] + ":00"  # Simplified hourly grouping
        if day in days and start_hour in grid:
            grid[start_hour][day] = f"[{cls.get('code', 'Class')}]"
            
    # Format for tabulate
    table_data = []
    for time in time_slots:
        row = [time] + [grid[time][day] for day in days]
        table_data.append(row)
        
    print("\n--- Weekly Timetable Preview ---")
    print(tabulate(table_data, headers=["Time"] + days, tablefmt="rounded_grid"))
