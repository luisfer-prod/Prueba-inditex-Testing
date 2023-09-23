import json

class MascotaAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def count_same_names(self):
        name_count = {}
        for record in self.data:
            name = record["name"]
            if name in name_count:
                name_count[name] += 1
            else:
                name_count[name] = 1
        filtered_names = {name: count for name, count in name_count.items() if count >= 2}
        return filtered_names


