from typing import List, Set


class CourseSchedule:
    """
    Problem Link: https://leetcode.com/problems/course-schedule/
    Complexity: Medium
    """

    validated_courses: Set = set()
    course_dependency_set: Set = set()
    course_requirements: List[List[int]]

    def are_course_requirements_valid(self, course_idx: int) -> bool:
        self.validated_courses.add(course_idx)
        self.course_dependency_set.add(course_idx)

        for required_course_idx in self.course_requirements[course_idx]:
            if required_course_idx in self.course_dependency_set:
                # cyclic dependency found in this course schedule
                return False

            if required_course_idx in self.validated_courses:
                # if we validated the course, then this means it has no contradictions
                continue

            if not self.are_course_requirements_valid(required_course_idx):
                # if we found contradictions, we may stop exploring dependency graph further
                return False

        self.course_dependency_set.remove(course_idx)

        return True

    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        self.validated_courses = set()
        self.course_requirements = [[] for _ in range(num_courses)]

        for dependant_course_idx, dependency_course_idx in prerequisites:
            self.course_requirements[dependant_course_idx].append(dependency_course_idx)

        for course_idx, requirements in enumerate(self.course_requirements):
            if course_idx in self.validated_courses:
                # course requirements tree has been already validated, so no contradictions were found there
                continue

            self.course_dependency_set: Set = set()

            if not self.are_course_requirements_valid(course_idx):
                # stop exploring the dependency graph at the very first contradiction
                return False

        return True
