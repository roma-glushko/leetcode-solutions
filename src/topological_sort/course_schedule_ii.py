from typing import List, Set


class CourseScheduleII:
    """
    Problem Link: https://leetcode.com/problems/course-schedule-ii/
    """
    validated_courses: Set = set()
    course_dependency_set: Set = set()
    course_requirements: List[List[int]]

    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        self.validated_courses = set()
        self.course_requirements = [[] for _ in range(num_courses)]

        for dependant_course_idx, dependency_course_idx in prerequisites:
            self.course_requirements[dependant_course_idx].append(dependency_course_idx)

        for course_idx, requirements in enumerate(self.course_requirements):
            pass

        return []
