"""
# Problem 2
Course Schedule (https://leetcode.com/problems/course-schedule/)
"""

from collections import deque
from typing import List

#TC : O( V + E) SC: O(V + E) V; vertices and E edges of the graph
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create adjacency list (graph) and in-degree array
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses  # Track number of prerequisites for each course

        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq → course
            in_degree[course] += 1  # Increment in-degree for dependent courses

        # Step 2: Initialize queue with courses that have no prerequisites (in-degree = 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Step 3: Process courses using BFS (Topological Sort)
        processed_courses = 0  # Count of courses we can complete

        while queue:
            course = queue.popleft()
            processed_courses += 1

            for next_course in graph[course]:
                in_degree[next_course] -= 1  # Reduce prerequisite count
                if in_degree[next_course] == 0:
                    queue.append(next_course)  # If no remaining prerequisites, add to queue

        # Step 4: If all courses are processed, we can finish all courses
        return processed_courses == numCourses
