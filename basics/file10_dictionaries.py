from log_variable import log_variable

"""
Mutable, Unordered set of key and values
Indexed by key
Cannot have list as unique key
"""
dict1 = {}
log_variable("type({})", type({}))

dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
log_variable("{\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}", {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"})

number_key_dict = {1: "First Element", 2: "Second element"}
log_variable("{1: \"First Element\", 2: \"Second element\"}", {1: "First Element", 2: "Second element"})

log_variable("{\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}[\"IOS\"]", {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}["IOS"])
log_variable("{\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}[\"Vendor\"]", {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}["Vendor"])

# Add a new key to the dictionary
dict1["RAM"] = "128"
log_variable("{\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}[\"RAM\"] = \"128\"", dict1)

# Updtate a key in the dictionary
dict1["IOS"] = "12.3"
log_variable("{\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}[\"IOS\"] = \"12.3\"", dict1)

# Deleting an entry
del dict1["Ports"]
log_variable("del {\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}[\"Ports\"]", dict1)

log_variable("len({\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"})", len({"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}))
log_variable("\"IOS\" in {\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}", "IOS" in {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"})
log_variable("\"IOS2\" in {\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}", "IOS2" in {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"})
log_variable("\"IOS2\" not in {\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}", "IOS2" not in {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"})

# The methods below keep de order used to create the key values set
log_variable("{\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}.keys()", {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}.keys())
log_variable("{\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}.values()", {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}.values())
log_variable("{\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}.items()", {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}.items())

# Retrieving Keys and List of keys
log_variable("type({\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}.keys())", type({"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}.keys()))
log_variable("list({\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}.keys())", list({"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}.keys()))

# Retrieving List of values
log_variable("type({\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}.values())", type({"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}.values()))
log_variable("list({\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}.values())", list({"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}.values()))

# Retrieving List of items
log_variable("type({\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}.items())", type({"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}.items()))
log_variable("list({\"Vendor\": \"Cisco\", \"Model\": \"2600\", \"IOS\": \"12.4\", \"Ports\": \"4\"}.items())", list({"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}.items()))