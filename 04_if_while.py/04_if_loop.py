yearly_salaries = [50_000, 70_000, 90_000, 110_000, 130_000]
high_salary_criteria = 100_000
count_of_high_salaries = 0
count_of_low_salaries = 0

for yearly_salary in yearly_salaries:
    if yearly_salary >= high_salary_criteria:
        count_of_high_salaries += 1
    else:
        count_of_low_salaries += 1

print("Count of high salaries:", count_of_high_salaries)
print("Count of low salaries:", count_of_low_salaries)
