class Assignment:
    def __init__(self, name, category, weight, grade):
        self.name = name
        self.category = category
        self.weight = weight
        self.grade = grade
        self.weighted_score = (grade / 100) * weight

class GradeCalculator:
    def __init__(self):
        self.assignments = []
        self.total_weights = {"Formative": 0, "Summative": 0}
        self.total_scores = {"Formative": 0, "Summative": 0}

    def add_assignment(self, name, category, weight, grade):
        if category not in ["Formative", "Summative"]:
            print("Invalid category! Must be Formative or Summative.")
            return
        if not (0 <= grade <= 100):
            print("Grade must be between 0 and 100.")
            return
        if not (0 < weight <= 100):
            print("Weight must be between 1 and 100.")
            return
        if self.total_weights[category] + weight > 100:
            print(f"Cannot add weight. {category} total weight would exceed 100%.")
            return

        assignment = Assignment(name, category, weight, grade)
        self.assignments.append(assignment)
        self.total_weights[category] += weight
        self.total_scores[category] += assignment.weighted_score
        print(f"Assignment '{name}' added successfully!\n")

    def calculate_gpa(self):
        total_weighted_score = sum(a.weighted_score for a in self.assignments)
        gpa = (total_weighted_score / 100) * 5
        return round(gpa, 2)

    def pass_or_fail(self):
        avg_formative = self.total_scores["Formative"]
        avg_summative = self.total_scores["Summative"]

        print("\n--- FINAL REPORT ---")
        print(f"Total Formative Grade: {avg_formative}%")
        print(f"Total Summative Grade: {avg_summative}%")
        print(f"GPA (out of 5): {self.calculate_gpa()}")

        if avg_formative >= 50 and avg_summative >= 50:
            print("Result: PASS ✅")
        elif avg_formative < 50 and avg_summative < 50:
            print("Result: FAIL ❌ - Repeat Course")
        else:
            print("Result: FAIL ❌ - One category is below average")

def main():
    gc = GradeCalculator()
    print("=== Grade Generator Calculator ===\n")

    while True:
        name = input("Enter assignment name: ")
        category = input("Enter category (Formative/Summative): ")
        try:
            weight = float(input("Enter weight (0-100): "))
            grade = float(input("Enter grade (0-100): "))
        except ValueError:
            print("Please enter valid numeric values.\n")
            continue

        gc.add_assignment(name, category, weight, grade)

        more = input("Do you want to add another assignment? (yes/no): ").lower()
        if more != 'yes':
            break

    gc.pass_or_fail()

if __name__ == "__main__":
    main()
