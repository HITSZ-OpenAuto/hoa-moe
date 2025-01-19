import json
from typing import Dict, TypedDict, Optional


class CourseData(TypedDict):
    card_string: str
    last_commit_sha: str
    has_error: bool


def create_course_data(card_string: str, last_commit_sha: str, has_error: bool = False) -> CourseData:
    """
    create a new course data
    :param card_string: the result of gen_links for each course
    :param last_commit_sha: last GitHub commit sha belongs to this course
    :param has_error: whether the course card generate steps has an error
    :return: the match course data, or None if no match found
    """
    if card_string is None:
        raise ValueError("card_string cannot be None")

    if last_commit_sha is None:
        raise ValueError("last_commit_sha cannot be None")

    return {
        "card_string": card_string,
        "last_commit_sha": last_commit_sha,
        "has_error": has_error,
    }


class FileTreeManager:
    def __init__(self):
        """Initialize FileTreeManager and load data from file"""
        with open('scripts/filetrees/filetrees.json', 'r') as file:
            self.file_trees = json.load(file)

    def save(self) -> None:
        """Save the current state to file"""
        with open('scripts/filetrees/filetrees.json', 'w', encoding="utf-8") as file:
            file.write(json.dumps(self.file_trees))

    def search(self, course_name: str) -> Optional[CourseData]:
        """
        Get the match course data:
        {
            "card_string": str,
            "last_commit_sha": str,
            "has_error": bool
        }
        :param course_name: HOA course name, e.g. EE1011A
        :return: the match course data, or None if no match found
        """
        return self.file_trees.get(course_name)  # More pythonic way to handle KeyError

    def add(self, course_name: str, filetree: CourseData) -> None:
        """
        Add a new course and its associated data
        :param course_name: HOA course name, e.g. EE1011A
        :param filetree: Course data containing card_string, last_commit_sha and has_error
        :raises ValueError: If course_name is empty or filetree is missing required fields
        :raises KeyError: If course already exists
        """
        if not course_name:
            raise ValueError("Course name cannot be empty")

        if not isinstance(filetree.get("card_string"), str) or not isinstance(filetree.get("last_commit_sha"), str):
            raise ValueError("Invalid filetree format")

        if course_name in self.file_trees:
            raise KeyError(f"Course {course_name} already exists. Use update() to modify existing courses.")

        self.file_trees[course_name] = filetree

    def update(self, course_name: str, filetree: CourseData) -> None:
        """
        Update an existing course's data
        :param course_name: HOA course name, e.g. EE1011A
        :param filetree: Course data containing card_string, last_commit_sha and has_error
        :raises ValueError: If course_name is empty or filetree is missing required fields
        :raises KeyError: If course doesn't exist
        """
        if not course_name:
            raise ValueError("Course name cannot be empty")

        if not isinstance(filetree.get("card_string"), str) or not isinstance(filetree.get("last_commit_sha"), str):
            raise ValueError("Invalid filetree format")

        if course_name not in self.file_trees:
            raise KeyError(f"Course {course_name} not found")

        self.file_trees[course_name] = filetree

    def delete(self, course_name: str) -> None:
        """
        Delete a course and its associated data
        :param course_name: HOA course name, e.g. EE1011A
        :raises KeyError: If course doesn't exist
        """
        if course_name not in self.file_trees:
            raise KeyError(f"Course {course_name} not found")

        del self.file_trees[course_name]

    def export_card_files(self) -> None:
        """
        Export individual txt files for each course's card string
        """
        for course_name, course_data in self.file_trees.items():
            file_name = f"{course_name}_cards.txt"
            with open(file_name, 'w') as file:
                file.write(course_data["card_string"])

