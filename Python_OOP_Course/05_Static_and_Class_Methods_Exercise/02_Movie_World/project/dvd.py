class DVD:
    def __init__(self, name, dvd_id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split(".")
        months_mapper = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May",
                         "06": "June", "07": "July", "08": "August", "09": "September", "10": "October",
                         "11": "November", "12": "December"}

        day, year = int(day), int(year)
        month = months_mapper[month]

        return cls(name, dvd_id, year, month, age_restriction)

    def __repr__(self):
        dvd_status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {dvd_status}"
