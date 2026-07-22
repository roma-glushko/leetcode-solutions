from .course_schedule import CourseSchedule


def test_possible_schedule_with_two_courses():
    solution = CourseSchedule()
    assert solution.canFinish(2, [[1, 0]])


def test_impossible_schedule_with_two_courses():
    solution = CourseSchedule()
    assert not solution.canFinish(2, [[1, 0], [0, 1]])


def test_possible_schedule_four_courses():
    solution = CourseSchedule()
    assert solution.canFinish(4, [[0, 1], [1, 3], [3, 2]])
