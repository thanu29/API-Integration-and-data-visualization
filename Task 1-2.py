# visualize the data in Healthcare.gov API
import matplotlib.pyplot as plt # using matplotlib
import seaborn as sns # using seaborn
from collections import Counter

data_API = [
    {'tags': ['glossary'], 'categories': ['glossary'], 'topics': [], 'title': 'Affordability Exemption'},
    {'tags': ['glossary', 'taxes'], 'categories': ['glossary'], 'topics': [], 'title': 'Tax Credits'},
    {'tags': ['public'], 'categories': ['policy'], 'topics': [], 'title': 'Medicaid Expansion'},
    {'tags': ['important', 'update'], 'categories': ['news'], 'topics': [], 'title': 'Open Enrollment Period'},
    {'tags': ['glossary'], 'categories': ['glossary'], 'topics': [], 'title': 'Individual Coverage HRA'},
    {'tags': ['state'], 'categories': ['policy'], 'topics': [], 'title': 'State Insurance Regulations'},
    {'tags': ['glossary'], 'categories': ['glossary'], 'topics': [], 'title': 'Premium Tax Credit'},
    {'tags': ['update'], 'categories': ['news'], 'topics': [], 'title': 'Enrollment Data Update'},
    {'tags': ['public', 'medicaid'], 'categories': ['policy'], 'topics': [], 'title': 'Medicaid Expansion'},
    {'tags': ['glossary'], 'categories': ['glossary'], 'topics': [], 'title': 'Cafeteria Plan'},

]
