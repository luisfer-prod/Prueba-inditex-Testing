from Objects.MatchingAnalizer import *
from Methods.MakeGetRequestParams import *

status = {"status":"available"}

url =  "https://petstore.swagger.io/v2/pet/findByStatus"

response_content = make_get_request(url,params=status)

data = json.loads(response_content)
    
analyzer = MascotaAnalyzer(data)

name_counts = analyzer.count_same_names()
    
print("Conteo de nombres:")
for name, count in name_counts.items():
        print(f"{name}: {count}")