from src.optimizer import find_best_ge_plan
from src.renderer import render_weekly_grid

def main():
    print("=== CityU Gateway Education Planner & Optimizer ===")
    
    # 1. Mock Student Schedule (loaded from JSON or user input)
    student_schedule = [
        {"day": "Mon", "start": "10:00", "end": "11:50"},
        {"day": "Wed", "start": "14:00", "end": "16:50"}
    ]
    
    # 2. Student Preferences
    preferences = {
        "desired_area": "Area 1",
        "min_free_days": 2
    }
    
    # 3. Sample GE Courses Database (Normally loaded from public catalog cache)
    ge_database = [
        {
            "code": "GE1105",
            "title": "Chinese Music Appreciation",
            "area": "Area 1",
            "sections": [{"day": "Tue", "start": "14:00", "end": "15:50"}]
        },
        {
            "code": "GE2109",
            "title": "Love, Sex, and Relationships",
            "area": "Area 1",
            "sections": [{"day": "Mon", "start": "10:00", "end": "11:50"}] # Clashes!
        }
    ]
    
    # 4. Run Optimization
    recommendations = find_best_ge_plan(ge_database, student_schedule, preferences)
    
    if recommendations:
        best_choice = recommendations[0]
        print(f"\nRecommended GE: {best_choice['code']} - {best_choice['title']}")
        print(f"Free Days Achieved: {best_choice['free_days_list']}")
        
        # 5. Render Visual Timetable
        render_weekly_grid(student_schedule, selected_ge_section=best_choice['section'])
    else:
        print("\nNo clash-free GE courses found matching your preferences.")

if __name__ == "__main__":
    main()
