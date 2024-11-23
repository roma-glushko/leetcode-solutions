from typing import List


class CourseScheduleII:
    """
    Problem Link: https://leetcode.com/problems/course-schedule-ii/
    Complexity: Medium

    Runtime: 104ms
    Memory: 17.1MB
    """

    # statuses of the course planning
    course_to_be_planned: int = 0
    course_in_planning: int = 1
    course_scheduled: int = 2

    def plan_course(self, course_idx: int, course_requirements: List[int]) -> List[int]:
        if self.course_status[course_idx] == self.course_scheduled:
            return []

        if self.course_status[course_idx] == self.course_in_planning:
            # loop has been detected
            raise ValueError("Requirement loop has been detected")

        self.course_status[course_idx] = self.course_in_planning

        course_schedule: List[int] = []

        for required_course_idx in course_requirements:
            course_schedule.extend(
                self.plan_course(
                    required_course_idx, self.course_requirements[required_course_idx]
                )
            )

        course_schedule.append(course_idx)
        self.course_status[course_idx] = self.course_scheduled

        return course_schedule

    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        self.course_schedule: List[int] = []
        self.course_status: List[int] = [self.course_to_be_planned] * num_courses
        self.course_requirements: List[List[int]] = [[] for _ in range(num_courses)]

        for dependant_course_idx, dependency_course_idx in prerequisites:
            self.course_requirements[dependant_course_idx].append(dependency_course_idx)

        for course_idx, requirements in enumerate(self.course_requirements):
            try:
                self.course_schedule.extend(self.plan_course(course_idx, requirements))
            except:  # noqa
                # requirement loop presents in the schedule
                return []

        return self.course_schedule
