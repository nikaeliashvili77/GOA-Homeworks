# str(), int(), და float() — ეს ფუნქციები Python-ში მონაცემთა ტიპების კონვერტაციისთვის გამოიყენება. მოდით, ვნახოთ მათი გამოყენების დეტალები და როგორ მუშაობენ ისინი

# str() — მონაცემის სტრინგად გადაქცევა
# str() ფუნქცია იყენებენ ნებისმიერი მონაცემის სტრინგად  გადაქცევას.

# text = str(number)
# print(text)  # "123"
# ამ შემთხვევაში, str() აიღებს ინტეგერს 123 და გადააკეთებს მას სტრინგად, რის შედეგადაც მიიღებთ "123". ნებისმიერ ტიპს 
# int() ფუნქცია იყენებენ ნებისმიერი ტიპის მონაცემის მთელ რიცხვად (integer) გადაქცევას. მას შეუძლია გამოიყენოს სტრინგი, თუ სტრინგი შეიცავს რიცხვებს.

# შეგახსენებთ: თუ სტრინგში არ იქნება მხოლოდ რიცხვები, ამ შემთხვევაში Python გამოიტანენ შეცდომას:
# text = "abc"
# number = int(text)  # ეს გამოიწვევს შეცდომას: ValueError
# float() — მონაცემის მექანიკური რიცხვად  გადაქცევა

 # float შეიცავს, სტრინგს, რომელიც შეიცავს მაჩვენებელს 