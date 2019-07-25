# Create a class called Payroll whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits.
# Create 5 different class methods which will calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, grossSalary and netSalary.


class Payroll:
    id = 0
    name = ""
    gender = ""
    gross_salary = 0
    tax = 0
    NSSF = 200
    taxable_gross = 0

    def __init__(self, id, name, gender, gross_salary, tax, NSSF, taxable_gross):
        self.id = id
        self.name = name
        self.gender = gender
        self.salary = gross_salary
        self.tax = tax
        self.NSSF = NSSF
        self.taxable_gross = taxable_gross

    def ss_fund(self):
        self.taxable_gross = self.gross_salary - 200
        return self.taxable_gross

    def payee(self):
        if self.taxable_gross > 0 and self.taxable_gross <= 12298:
            self.tax = self.taxable_gross * 10/100
        elif self.taxable_gross > 12298 and self.taxable_gross <= 23885:
            self.tax = self.taxable_gross * 15/100
        elif self.taxable_gross > 23885 and self.taxable_gross <= 35472:
            self.tax = self.taxable_gross * 20/100
        elif self.taxable_gross > 35472 and self.taxable_gross <= 47059:
            self.tax = self.taxable_gross * 25/100
        elif self.taxable_gross > 47059:
            self.tax = self.taxable_gross * 30/100

        self.tax = self.tax + 1408
        return self.tax


emp1 = Payroll(1, 'Jon', 'M', 100000)

print(emp1.name)
print(emp1.tax)
