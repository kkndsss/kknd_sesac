from task1 import Student

## 문제 2: 성적 계산 기능 추가
class GradedStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)
  
    def calculate_average(self):

        # scores 리스트의 평균을 계산하여 반환하는 메서드를 작성하세요.
        # YOUR CODE HERE


        total = 0
        for score in self.scores:
          #일단 하나씩 꺼내서 더해
          total+= score #다 더함
        average =  total / len(self.scores) #평균 내고 출력
        print(f"평균 {average}")


    def study(self, hours):
        super().study(hours)


        # 공부한 시간에 비례하여 임의의 점수를 생성하고 add_score 메서드를 호출하세요.
        # 기본점수 : 60점, 최대 추가 점수 : 40점
        # 최대 공부시간 8시간으로 시간에 비례해서 점수 추가
        # YOUR CODE HERE
        #60+(공부시간/8)*40
        #최대 공부시간 이상이어도 100점이 될 수 있게.


        if hours > 8 :
          hours = 8
        basesco=60
        addsco = (hours / 8) * 40
        totalsco = basesco + addsco
        self.add_score(totalsco)


# GradedStudent 클래스의 객체를 생성하고, 여러 번 study 메서드를 호출한 후 평균 점수를 계산해보세요.
# YOUR CODE HERE

stu1 = GradedStudent("가렌", 20, 2)
stu1.study(2)
stu1.study(5)
stu1.study(10)
stu1.study(3)
stu1.calculate_average()