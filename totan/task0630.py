import random
import datetime

def generate_addition_subtraction_no_carry():
    questions = set()
    while len(questions) < 5:
        x = random.randint(0, 1)
        y = random.randint(1, 9)
        m = random.randint(0, 1)
        n = random.randint(1, 9)

        if x == 0 and m == 0:
            continue

        if x == m and y == n:
            continue

        operators = random.choice(["+", "-"])
        if operators == "+":
            if y + n >= 10:
                continue
            question = f"{10 * x + y} + {10 * m + n} = "
        else:
            if x < m or (x == m and y <= n):
                continue
            question = f"{10 * x + y} - {10 * m + n} = "

        questions.add(question)

    return questions

def generate_addition_subtraction_with_carry():
    questions = set()
    while len(questions) < 5:
        x = random.randint(0, 1)
        y = random.randint(1, 9)
        m = random.randint(0, 1)
        n = random.randint(1, 9)

        if m > x or (m == x and n >= y):
            continue

        operators = random.choice(["+", "-"])
        if operators == "+":
            if y + n <= 10:
                continue
            question = f"{10 * x + y} + {10 * m + n} = "
        else:
            if y >= n:
                continue
            question = f"{10 * x + y} - {10 * m + n} = "

        questions.add(question)

    return questions

def generate_addition_subtraction_within_100():
    questions = set()
    while len(questions) < 20:
        a = random.randint(10, 99)
        b = random.randint(2, 9)

        operators = random.choice(["+", "-"])
        if operators == "+":
            result = a + b
            question = f"{a} + {b} = "
        else:
            result = a - b
            if result < 0:
                continue
            question = f"{a} - {b} = "
        
        questions.add(question)
    
    return questions

def generate_addition_subtraction_up_to_100():
    questions = set()
    while len(questions) < 20:
        a = random.randint(10, 99)
        b = random.randint(10, 99)

        operators = random.choice(["+", "-"])
        if operators == "+":
            result = a + b
            question = f"{a} + {b} = "
        else:
            result = a - b
            if result < 0:
                continue
            question = f"{a} - {b} = "
        
        questions.add(question)
    
    return questions

def generate_three_digit_addition_subtraction():
    questions = set()
    while len(questions) < 20:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        c = random.randint(1, 99)

        operators = random.choice(["+++", "++-", "+-+", "+--", "-++", "-+-"])

        if operators == "+++":
            result = a + b + c
            question = f"{a} + {b} + {c} = "
        elif operators == "++-":
            result = a + b - c
            if result <= 0:
                continue
            question = f"{a} + {b} - {c} = "
        elif operators == "+-+":
            result = a + b + c
            question = f"{a} + {b} + {c} = "
        elif operators == "+--":
            result = a + b - c
            if result <= 0:
                continue
            question = f"{a} + {b} - {c} = "
        elif operators == "-++":
            result = a - b + c
            if result <= 0:
                continue
            question = f"{a} - {b} + {c} = "
        elif operators == "-+-":
            result = a - b - c
            if result <= 0:
                continue
            question = f"{a} - {b} - {c} = "
        
        questions.add(question)
    
    return questions

def generate_nested_operations_no_minus_first():
    questions = set()
    while len(questions) < 50:
        equation_type = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)

        if equation_type in [1, 2]:
            question = f"({random.randint(1, 100)}) + {a} = {b}"
        elif equation_type in [3, 4]:
            question = f"({random.randint(1, 100)}) + {a} - {b} = {c}"
        elif equation_type in [5, 6, 7, 8]:
            question = f"({random.randint(1, 100)}) - {a} = {b}"
        elif equation_type in [9, 10, 11, 12]:
            question = f"{a} + ({random.randint(1, 100)}) = {b}"
        elif equation_type in [13, 14, 15, 16, 17, 18, 19, 20]:
            question = f"{a} - ({random.randint(1, 100)}) = {b}"

        questions.add(question)

    return questions


def generate_multiplication():
    questions = set()
    while len(questions) < 20:
        a = random.randint(2, 9)
        b = random.randint(2, 9)

        question = f"{a} × {b} = "
        questions.add(question)
    
    return questions

def generate_division():
    questions = set()
    while len(questions) < 20:
        a = random.randint(1, 99)
        b = random.randint(2, 9)

        if a % b != 0 or a // b <= 1 or a // b >= 10:
            continue

        question = f"{a} ÷ {b} = "
        questions.add(question)

    return questions

def generate_weekly_homework():
    now = datetime.datetime.now()
    start_date = now.date()
    end_date = start_date + datetime.timedelta(days=6)

    for i in range(30):
        current_date = start_date + datetime.timedelta(days=i)
        markdown_content = f"# Weekly Homework ({current_date})\n\n"

        markdown_content += "## Addition and Subtraction (No Carry)\n\n"
        questions = generate_addition_subtraction_no_carry()
        markdown_content += "\n".join(questions)
        markdown_content += "\n\n"

        markdown_content += "## Addition and Subtraction (With Carry)\n\n"
        questions = generate_addition_subtraction_with_carry()
        markdown_content += "\n".join(questions)
        markdown_content += "\n\n"

        markdown_content += "## Addition and Subtraction (Within 100)\n\n"
        questions = generate_addition_subtraction_within_100()
        markdown_content += "\n".join(questions)
        markdown_content += "\n\n"

        markdown_content += "## Addition and Subtraction (Up to 100)\n\n"
        questions = generate_addition_subtraction_up_to_100()
        markdown_content += "\n".join(questions)
        markdown_content += "\n\n"

        markdown_content += "## Three-Digit Addition and Subtraction\n\n"
        questions = generate_three_digit_addition_subtraction()
        markdown_content += "\n".join(questions)
        markdown_content += "\n\n"

        markdown_content += "## Nested Operations (No Minus First)\n\n"
        questions = generate_nested_operations_no_minus_first()
        markdown_content += "\n".join(questions)
        markdown_content += "\n\n"

        markdown_content += "## Multiplication\n\n"
        questions = generate_multiplication()
        markdown_content += "\n".join(questions)
        markdown_content += "\n\n"

        markdown_content += "## Division\n\n"
        questions = generate_division()
        markdown_content += "\n".join(questions)

        file_name = f"weekly_homework_{current_date}.txt"
        with open(file_name, "w") as file:
            file.write(markdown_content)

        print(f"Weekly homework for {current_date} generated and saved as '{file_name}'.")

generate_weekly_homework()
