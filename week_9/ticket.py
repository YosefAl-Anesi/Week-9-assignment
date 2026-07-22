def create_ticket():
    print("=== IT Helpdesk Ticket ===")
    student_name = input("Student Name : ")
    student_id = input("Student ID   : ")
    issue = input("Issue        : ")
    location = input("Location     : ")
    priority = input("Priority (High/Medium/Low): ")

    # Priority assignment logic
    priority_clean = priority.strip().capitalize()
    if priority_clean == "High":
        technician = "Ahmad"
    elif priority_clean == "Medium":
        technician = "Siti"
    elif priority_clean == "Low":
        technician = "Ali"
    else:
        technician = "Unassigned"

    status = "Pending"

    return {
        "student_name": student_name,
        "student_id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
        "technician": technician,
        "status": status
    }
