
# Alexander J. Jackson
# loan_qualifier.py

salary = int(input("Please input your salary: "))
years_on_job = int(input("Please enter years on the job: "))

if salary >= 30000:
	if years_on_job >= 2:
		print("You qualify for the loan.")
	else:
		print("You must hafe been on your current job for at least two years to qualify.")
else:
	print("You must earn at least $30,000 per year to qualify.")
