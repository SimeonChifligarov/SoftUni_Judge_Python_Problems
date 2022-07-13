from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        current_category = [c for c in self.categories if c.id == category_id][0]
        current_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = [t for t in self.topics if t.id == topic_id][0]
        current_topic.topic = new_topic
        current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        current_document = [d for d in self.documents if d.id == document_id][0]
        current_document.file_name = new_file_name

    def delete_category(self, category_id):
        current_category = [c for c in self.categories if c.id == category_id][0]
        if current_category in self.categories:
            self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = [t for t in self.topics if t.id == topic_id][0]
        if current_topic in self.topics:
            self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_document = [d for d in self.documents if d.id == document_id][0]
        if current_document in self.documents:
            self.documents.remove(current_document)

    def get_document(self, document_id):
        current_document = [d for d in self.documents if d.id == document_id][0]
        return current_document

    def __repr__(self):
        return "\n".join([repr(doc) for doc in self.documents])
