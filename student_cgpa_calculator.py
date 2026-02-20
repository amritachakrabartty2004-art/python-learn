import os

# Grade to Grade Point Mapping
# O  = 10
# A+ = 9
# A  = 8
# B+ = 7
# B  = 6
# C  = 5
# F  = 0
GRADE_MAPPING = {
    'O': 10,
    'A+': 9,
    'A': 8,
    'B+': 7,
    'B': 6,
    'C': 5,
    'F': 0
}

def get_valid_input(prompt, validation_func, error_message):
    """
    Utility function to get valid input from user.
    Uses a while loop to keep asking until the validation_func returns True.
    """
    while True:
        try:
            val = input(prompt).strip()
            if validation_func(val):
                return val
            else:
                print(f"Error: {error_message}")
        except Exception:
            print(f"Error: {error_message}")

def calculate_semester_cgpa(semester_num):
    """
    Calculates CGPA for a single semester and returns a dictionary containing all details.
    This function handles input for each subject in the semester.
    """
    print(f"\n--- Entering Details for Semester {semester_num} ---")
    
    # Input: Number of subjects with validation
    num_subjects_str = get_valid_input(
        "Enter number of subjects: ",
        lambda x: x.isdigit() and int(x) > 0,
        "Please enter a positive integer greater than zero."
    )
    num_subjects = int(num_subjects_str)

    subjects = []
    total_weighted_points = 0
    total_credits = 0
    backlogs = []

    # Loop through each subject
    for i in range(num_subjects):
        print(f"\nSubject {i+1}:")
        name = input("  Enter subject name: ").strip()
        if not name:
            name = f"Subject {i+1}" # Default name if empty
        
        # Input: Subject credit with validation
        credit_str = get_valid_input(
            "  Enter subject credit (e.g., 3, 4): ",
            lambda x: x.replace('.','',1).isdigit() and float(x) > 0,
            "Please enter a valid positive number for credits."
        )
        credit = float(credit_str)

        # Input: Grade with validation
        grade = get_valid_input(
            f"  Enter grade ({', '.join(GRADE_MAPPING.keys())}): ",
            lambda x: x.upper() in GRADE_MAPPING,
            "Invalid grade. Please choose from O, A+, A, B+, B, C, F."
        ).upper()

        # Grade mapping logic
        grade_point = GRADE_MAPPING[grade]
        total_weighted_points += (credit * grade_point)
        total_credits += credit

        # Store subject details
        subjects.append({
            'name': name,
            'credit': credit,
            'grade': grade,
            'grade_point': grade_point
        })

        # Backlog Detection
        if grade == 'F':
            backlogs.append(name)

    # CGPA Calculation: sum(Credit * GradePoint) / sum(Credits)
    cgpa = total_weighted_points / total_credits if total_credits > 0 else 0
    
    # Percentage Calculation: CGPA * 9.5
    percentage = cgpa * 9.5
    
    # Pack semester data into a dictionary
    semester_data = {
        'semester_num': semester_num,
        'subjects': subjects,
        'total_credits': total_credits,
        'total_weighted_points': total_weighted_points,
        'cgpa': cgpa,
        'percentage': percentage,
        'backlogs': backlogs
    }

    return semester_data

def display_semester_report(data):
    """
    Prints a clear and formatted semester report to the console.
    """
    print("\n" + "="*45)
    print(f"          REPORT FOR SEMESTER {data['semester_num']} ")
    print("="*45)
    print(f"Total Credits:       {data['total_credits']:.2f}")
    print(f"Total Grade Points:  {data['total_weighted_points']:.2f}")
    print(f"Semester CGPA:       {data['cgpa']:.2f}")
    print(f"Percentage:          {data['percentage']:.2f}%")
    
    # Backlog status display
    if data['backlogs']:
        print(f"Status:              FAIL (Backlog Detected)")
        print(f"Backlog in:          {', '.join(data['backlogs'])}")
    else:
        print(f"Status:              PASS")
        print(f"Backlog Detection:   No Backlogs")
    print("="*45)

def save_to_file(all_semesters_data, overall_cgpa, overall_percentage):
    """
    Saves the final project report to a text file 'cgpa_report.txt'.
    """
    filename = "cgpa_report.txt"
    try:
        with open(filename, "w") as f:
            f.write("========================================\n")
            f.write("        STUDENT CGPA PROJECT REPORT     \n")
            f.write("========================================\n\n")
            
            for data in all_semesters_data:
                f.write(f"--- SEMESTER {data['semester_num']} details ---\n")
                f.write(f"Total Credits:       {data['total_credits']:.2f}\n")
                f.write(f"Total Grade Points:  {data['total_weighted_points']:.2f}\n")
                f.write(f"CGPA:                {data['cgpa']:.2f}\n")
                f.write(f"Percentage:          {data['percentage']:.2f}%\n")
                if data['backlogs']:
                    f.write(f"Backlogs:            {', '.join(data['backlogs'])}\n")
                else:
                    f.write("Backlogs:            No Backlogs\n")
                f.write("-" * 40 + "\n")
            
            f.write(f"\nFINAL OVERALL SUMMARY\n")
            f.write(f"Overall Cumulative CGPA:  {overall_cgpa:.2f}\n")
            f.write(f"Overall Percentage:       {overall_percentage:.2f}%\n")
            
            has_any_backlog = any(d['backlogs'] for d in all_semesters_data)
            f.write(f"Overall Pass Status:      {'FAIL' if has_any_backlog else 'PASS'}\n")
            f.write("\nGenerated by: Student CGPA Calculator System\n")
        
        print(f"\n[+] Success: Final report saved to '{filename}'")
    except Exception as e:
        print(f"\n[-] Error saving to file: {e}")

def main():
    """
    Entry point of the program.
    Coordinates multiple semester calculations and displays overall summary.
    """
    os.system('cls' if os.name == 'nt' else 'clear') # Clear screen for better UI
    
    print("************************************************")
    print("*                                              *")
    print("*        STUDENT CGPA CALCULATOR PROJECT       *")
    print("*                                              *")
    print("************************************************")

    # Storage for multiple semesters (Bonus Feature)
    all_semesters_data = []
    
    # Input: Number of semesters
    num_sem_str = get_valid_input(
        "Enter number of semesters to calculate: ",
        lambda x: x.isdigit() and int(x) > 0,
        "Please enter a positive integer."
    )
    num_semesters = int(num_sem_str)

    # Process each semester
    for i in range(1, num_semesters + 1):
        sem_data = calculate_semester_cgpa(i)
        all_semesters_data.append(sem_data)
        display_semester_report(sem_data)

    # Calculate Overall Cumulative CGPA (Bonus Feature)
    total_points = sum(d['total_weighted_points'] for d in all_semesters_data)
    total_overall_credits = sum(d['total_credits'] for d in all_semesters_data)
    
    overall_cgpa = total_points / total_overall_credits if total_overall_credits > 0 else 0
    overall_percentage = overall_cgpa * 9.5

    # Final Overall Summary Display
    print("\n" + "#"*45)
    print("             FINAL OVERALL SUMMARY             ")
    print("#"*45)
    print(f"Total Credits (All Semesters): {total_overall_credits:.2f}")
    print(f"Cumulative Overall CGPA:       {overall_cgpa:.2f}")
    print(f"Overall Percentage:            {overall_percentage:.2f}%")
    
    has_any_backlog = any(d['backlogs'] for d in all_semesters_data)
    if has_any_backlog:
        print(f"Final Status:                  FAIL (Backlogs detected)")
    else:
        print(f"Final Status:                  PASS (No Backlogs)")
    print("#"*45)

    # Save to file option (Bonus Feature)
    save_choice = input("\nDo you want to save the complete report to a file? (y/n): ").strip().lower()
    if save_choice == 'y':
        save_to_file(all_semesters_data, overall_cgpa, overall_percentage)

    print("\nThank you for using the CGPA Calculator! Good luck with your studies.")

if __name__ == "__main__":
    main()
