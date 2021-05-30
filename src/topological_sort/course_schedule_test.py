from unittest import TestCase

from .course_schedule import CourseSchedule


class CourseScheduleTest(TestCase):

    def test_possible_schedule_with_two_courses(self):
        solution = CourseSchedule()

        self.assertTrue(solution.canFinish(2, [[1, 0]]))

    def test_impossible_schedule_with_two_courses(self):
        solution = CourseSchedule()

        self.assertFalse(solution.canFinish(2, [[1, 0], [0, 1]]))

    def test_possible_schedule_four_courses(self):
        solution = CourseSchedule()

        self.assertTrue(solution.canFinish(4, [[0, 1], [1, 3], [3, 2]]))