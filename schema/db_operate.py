#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/8/26 14:39
# @Author     : fany
# @Project    : PyCharm
# @File       : db_operate.py
# @description:
from models import db, Student, Grade, Teacher, Course
# 增加数据
def insert_data():
    s = Student(name='李四',gender="男",phone="12345678901")
    s2 = Student(name='张三', gender="女", phone="12345678019")
    # 添加单个
    # db.session.add(s)
    # 添加多个
    db.session.add_all([s,s2])
    db.session.commit()

# 查
def get_data():
    # s = Student.query.get(2)    # 2 表示id
    # print(s.phone)

    #查所有
    # s = Student.query.all()
    # for i in s:
    #     print(i.name, i.phone)

    #filter() 条件查询
    # s = Student.query.filter(Student.id == 3)
    # for i in s:
    #     print(i.name)

    # filter_by 类似sql查询,  frist()查询到的第一个
    s = Student.query.filter_by(name = "张三").filter(Student.id == 3)
    for i in s:
        print(i.name)


# 改
def alter_data():
    # ①
    s = Student.query.filter(Student.gender == "男").update({"gender":"女"})  # 返回动了多少条数据
    db.session.add(s)
    db.session.commit()

    # ②
    s = Student.query.filter(Student.gender == "男").frist() #frist() 为1条数据,.all()为多条数据,需要遍历
    s.gender='男'
    db.session.add(s)
    db.session.commit()

# 删除只需将update改为delete


#一对多
def insert_data2():
    s = Grade(grade=10, student_id = 1)
    s2 = Grade(grade=15, student_id = 1)
    # 添加单个
    # db.session.add(s)
    # 添加多个
    db.session.add_all([s,s2])
    db.session.commit()

# 查询,
def get_data2():
    # 一访问多,
    # s = Student.query.get(1)
    # for i in s.grades:
    #     print(s.name,i.grade)
    # 多访问一
    s = Grade.query.filter(Grade.grade == 10).all()
    for i in s:
        print(i.student.name,i.student.gender)

# 多对多
student0 = Student(name="李玲", gender="女", phone="12345678900")
student1 = Student(name="李依", gender="女", phone="12345678901")
student2 = Student(name="李贰", gender="男", phone="12345678902")
student3 = Student(name="李叁", gender="男", phone="12345678903")
student4 = Student(name="李斯", gender="男", phone="12345678904")
student5 = Student(name="李舞", gender="女", phone="12345678905")
student6 = Student(name="李榴", gender="男", phone="12345678906")
student7 = Student(name="李淇", gender="女", phone="12345678907")
student8 = Student(name="李巴", gender="男", phone="12345678908")
student9 = Student(name="李玖", gender="男", phone="12345678909")

teacher0 = Teacher(name="老数", gender="男", phone="12345678910")
teacher1 = Teacher(name="老语", gender="女", phone="12345678911")
teacher2 = Teacher(name="老英", gender="女", phone="12345678912")
teacher3 = Teacher(name="老物", gender="男", phone="12345678913")
teacher4 = Teacher(name="老化", gender="男", phone="12345678914")
teacher5 = Teacher(name="老生", gender="男", phone="12345678915")

course0 = Course(name="数学")
course1 = Course(name="语文")
course2 = Course(name="英语")
course3 = Course(name="物理")
course4 = Course(name="化学")
course5 = Course(name="生物")

# 多对多操作
def all_to_all():
    #添加数据
    # db.session.add_all(
    #     [student0, student1, student2, student3, student4, student5, student6, student7, student8, student9, teacher0,
    #      teacher1, teacher2, teacher3, teacher4, teacher5, course0, course1, course2, course3, course4, course5])
    # db.session.commit()
    # 修改数据
    # for i in range(1, 7):
    #     c = Course.query.filter(Course.id == i).update({"teacher_id": i})
    #     print(c)
    # db.session.commit()
    # 查询课程表
    cs = Course.query.filter(Course.id >= 2).all()
    # print(cs)
    # 查询学生
    # stu = Student.query.filter(Student.id >= 2).all()
    # for s in stu:
          #修改课程表
    #     s.courses = cs
    #     print(s.courses)
    #     db.session.add(s)
    #     db.session.commit()

    # 学生查询课程
    # st = Student.query.get(1)
    # for s in st.courses:
    #     print(s.name)
    # print(st.courses)

    # 课程查询学生
    c = Course.query.get(2)
    for s in c.students:
        print(s.name)

if __name__ == '__main__':
    # insert_data()
    # get_data()
    # insert_data2()
    # get_data2()
    all_to_all()