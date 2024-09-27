# Melinda-Text-Dataset
Official repository for the Opensource Text dataset for NMT for local languages in West Africa (EWE Corpus) and implement the Yodi model after hand. 

Note: This repository will evolve into the official repository for the Yodi model, once the necessary data is gathered.

# Objective

##### • Develop a Machine Translation Text and Speech Dataset NMT for local languages in West Africa (EWE Corpus)

# Key Results 

###### -> Develop & Measure the accuracy or the performance of the Yodi model from this dataset for text-to-text translation.

###### -> Develop & Measure the accuracy of Yodi built from this dataset for Speech recognition.

##### Remark: Getting accurate data and labeled data from available sources online or in local written papers would be necessary for machine sentence translation. 

## Using the Updated Dictionaries

We have transformed and analyzed two Ewe-English dictionaries: KABDICT525 and EWEDICT995. These dictionaries are now available as Python modules for easy integration into your projects.

### Accessing the Dictionaries

1. The transformed dictionaries are located in the `Dictionaries` folder:
   - `Dictionaries/kabdict525.py`
   - `Dictionaries/ewedict995.py`

2. To use these dictionaries in your Python scripts, you can import them as follows:

```python
from Dictionaries.kabdict525 import ewe_to_english as kabdict
from Dictionaries.ewedict995 import ewe_to_english as ewedict

# Example usage
print(kabdict.get('word', 'Word not found'))
print(ewedict.get('word', 'Word not found'))

# Ongoing
![Dataset Analytics png](https://github.com/Umbaji/NMT-Melinda--Dataset/assets/125580751/48cd7ba5-bbb8-4eb4-b04f-8d901be176a1)

![image](https://github.com/Umbaji/NMT-Melinda--Dataset/assets/125580751/2850be94-fd74-4f61-b757-fc228a5c61b4)


Feel free to share your analytics in the discussions!
Instructions are available in project_contributions_instructions.txt

Please register at https://sites.google.com/umbaji.org/yodi/home to build the 
largest NMT text Dataset for West Africa.


