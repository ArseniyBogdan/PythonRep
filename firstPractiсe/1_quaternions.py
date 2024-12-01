import math
import unittest


class Quaternion(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __abs__(self):
        return (self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2) ** (1 / 2)

    def __str__(self):
        return "(" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ", " + str(self.d) + ")"

    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __sub__(self, other):
        return Quaternion(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)

    def __mul__(self, other):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = other.a
        y = other.b
        z = other.c
        t = other.d
        return Quaternion((a * x - b * y - c * z - d * t),
                          (a * y + b * x + c * t - d * z),
                          (a * z + c * x - b * t + d * y),
                          (a * t + d * x + b * z - c * y))

    def conjugate(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def norm(self):
        if abs(self) == 0:
            return
        else:
            return Quaternion(self.a / abs(self), self.b / abs(self), self.c / abs(self), self.d / abs(self))

    def __truediv__(self, other):
        q = self * (other.conjugate())
        denom = ((abs(other)) ** 2)
        if denom == 0:
            raise ZeroDivisionError('Division by zero. Quaternion norm must be bigger than 0')  # деление на 0
        return Quaternion(q.a / denom, q.b / denom, q.c / denom, q.d / denom)

    def quat_rotate(self, rotator):
        if self.a != 0:  # не чисто мнимый кватернион
            raise NotImQuatException("You can rotate just imaginary quaternion")
        return (rotator.norm() * self) * (rotator.norm()).conjugate()

    def angle_axis_rotate(self, axis, angle):
        if axis.a != 0:  # не чисто мнимый кватернион
            raise NotImQuatException("Rotation vector should be imaginary quaternion.")
        if self.a != 0:  # не чисто мнимый кватернион
            raise NotImQuatException("You can rotate just imaginary quaternion")
        n_axis = axis.norm()
        q = Quaternion(math.cos(angle / 2),
                       math.sin(angle / 2) * n_axis.b,
                       math.sin(angle / 2) * n_axis.c,
                       math.sin(angle / 2) * n_axis.d)
        return self.quat_rotate(q)

    def __eq__(self, other):
        return (self.a, self.b, self.c, self.d) == (other.a, other.b, other.c, other.d)


class NotImQuatException(Exception):  # исключение для не чисто мнимого кватерниона,

    pass


class Tester(unittest.TestCase):
    def setUp(self):
        self.q1 = Quaternion(0, 2.7, 9.8, 7.7)
        self.q2 = Quaternion(1, -2, -3, 4)

    def tearDown(self):
        print("\nTest case completed. Result:")

    def test_sum(self):
        q_sum = Quaternion(1, 0.7, 6.8, 11.7)
        print(self.q1 + self.q2, "expected", q_sum)

    def test_sub(self):
        q_sub = Quaternion(-1, 4.7, 12.8, 3.7)
        print(self.q1 - self.q2, "expected", q_sub)

    def test_mul(self):
        q_mul = (4.0, 65.0, -16.4, 19.2)
        print(self.q1 * self.q2, "expected", q_mul)

    def test_div(self):
        q_div = Quaternion(-0.13333333333333344, -1.9866666666666668, 1.2, -0.12666666666666668)
        print(self.q1 / self.q2, "expected", q_div)
        # print(q1 / Quaternion(0, 0, 0, 0))  # деление на 0

    def test_rotate(self):
        print("rotate by quaternion: ", self.q1.quat_rotate(self.q2))
        print("rotate by axis and angle: ", self.q1.angle_axis_rotate(Quaternion(0, 0, 0, 1), math.pi / 3))
        # print(q1.angle_axis_rotate(Quaternion(1, 0, 0, 0), math.pi / 3))  # вращение вокруг не чисто мнимого кватерниона


if __name__ == "__main__":
    unittest.main()

