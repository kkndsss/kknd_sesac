from task2 import GradedStudent

## 문제 3: 다중 상속을 이용한 운동선수 학생 클래스

class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def train(self, hours):
        print(f"{self.sport} 종목에서 {hours}시간 동안 훈련했습니다.")

class StudentAthlete(GradedStudent, Athlete):
    def __init__(self, name, age, grade, sport):
        # GradedStudent와 Athlete의 __init__ 메서드를 모두 호출하세요.
        # YOUR CODE HERE
        #super()써보려니까 안된다....
        #pass 써보려고 해도 매서드 오버라이딩 때문에 불가.
        #하나씩 불러와야한다.
        GradedStudent.__init__(self, name, age, grade)
        Athlete.__init__(self, sport)


    def study(self, hours):
        # GradedStudent의 study 메서드를 호출하고, 추가로 train 메서드도 호출하세요. 이때 훈련은 공부시간의 절반만큼 훈련
        # YOUR CODE HERE
        GradedStudent.study(self, hours)
        #GradedStudent.study의 시간을 가져와서 나눈 다음 train 매소드에 저장하고 출력
        train_hours= hours / 2
        self.train(train_hours)


# StudentAthlete 클래스의 객체를 생성하고 study 메서드를 호출해보세요.
# YOUR CODE HERE

if __name__ =="__main__":

    SH1=StudentAthlete("이즈리얼", 30, 5, "원딜")
    SH1.study(10)