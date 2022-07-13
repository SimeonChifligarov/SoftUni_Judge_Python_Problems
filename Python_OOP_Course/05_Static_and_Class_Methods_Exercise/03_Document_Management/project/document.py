from project.category import Category
from project.topic import Topic


class Document:
    def __init__(self, document_id, category_id, topic_id, file_name):
        self.id = document_id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, doc_id: int, category: Category, topic: Topic, file_name: str):
        return cls(doc_id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        if tag_content in self.tags:
            return

        self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        tags_result = ", ".join(self.tags)
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, " \
               f"topic {self.topic_id}, tags: {tags_result}"
