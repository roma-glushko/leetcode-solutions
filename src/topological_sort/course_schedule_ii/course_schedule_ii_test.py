from .course_schedule_ii import CourseScheduleII


def test_possible_schedule_with_two_courses():
    solution = CourseScheduleII()
    assert solution.findOrder(2, [[1, 0]]) == [0, 1]


def test_possible_one_course():
    solution = CourseScheduleII()
    assert solution.findOrder(1, []) == [0]


def test_impossible_schedule_with_two_courses():
    solution = CourseScheduleII()
    assert (
        solution.findOrder(
            5, [[0, 1], [0, 4], [4, 3], [4, 2], [4, 1], [2, 1], [1, 3], [3, 2]]
        )
        == []
    )


def test_possible_schedule_courses():
    solution = CourseScheduleII()
    assert solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert solution.findOrder(5, [[1, 0], [0, 2], [2, 3], [4, 1]]) == [3, 2, 0, 1, 4]
    assert solution.findOrder(5, [[0, 1], [0, 4], [4, 3], [4, 2], [4, 1], [2, 1]]) == [
        1,
        3,
        2,
        4,
        0,
    ]
