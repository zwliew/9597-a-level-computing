#!/usr/bin/env python3

def process_data():
    grades = {}
    with open('overall_grades.txt') as file:
        for line in file:
            line = line.rstrip()
            parts = line.split(';')
            name = parts[0]
            grades[name] = {}
            for part in parts:
                if part == name or part == '':
                    continue

                subject_name, subject_grades = part.split(':')
                subject_grades = subject_grades.split(',')
                grades[name][subject_name] = subject_grades

    return grades

def have_n_improvement(data, n):
    improved = []
    for k,v in data.items():
        num_improved = 0
        for grades in v.values():
            if grades[1] < grades[0]:
                num_improved += 1
        if num_improved == n:
            improved.append(k)
    return improved

def have_improvement_in_all_subjs(data):
    improved = []
    for k,v in data.items():
        num_improved = 0
        for grades in v.values():
            if grades[1] < grades[0]:
                num_improved += 1
        if num_improved == len(v):
            improved.append(k)
    return improved

def count_combi(data, combi):
    total = 0
    for k,v in data.items():
        subjects = list(v.keys())
        is_subset = True
        for subject in combi:
            if subject not in subjects:
                is_subset = False
                break
        if is_subset:
            total += 1
    return total

def calculate_GPA(grades, name):
    points_dict = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

    subjects = grades[name]
    total_subjects = len(subjects)
    total_points = 0

    for grades in subjects.values():
        total_points += points_dict[grades[0]]
        total_points += points_dict[grades[1]]

    return total_points / total_subjects / 2

def main():
    grades = process_data()
    improved = have_n_improvement(grades, 1)
    all_improved = have_improvement_in_all_subjs(grades)
    combis = count_combi(grades, ['EL', 'Math'])

    # Finding the total number fo students who take Chem and Bio but not Physics
    chem_bio_count = count_combi(grades, ['Chem', 'Bio'])
    chem_bio_physics_count = count_combi(grades, ['Chem', 'Bio', 'Phy'])
    chem_bio_no_physics_count = chem_bio_count - chem_bio_physics_count
    print(chem_bio_no_physics_count, 'students take Chemistry and Biology but not Physics.')

    gpa = calculate_GPA(grades, 'Claudette Bode')
    print(gpa)

main()
