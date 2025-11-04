import json
with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("DN                                                 Description           Speed    MTU")
print("-" * 80)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    print(f"{attr['dn']:50} {attr['descr']:20} {attr['speed']:8} {attr['mtu']:6}")                         