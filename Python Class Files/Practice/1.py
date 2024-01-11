import importlib.metadata
import os

package_info = importlib.metadata.metadata('requests')

print(package_info)

info = os.stat('D:\Python Projects\Python Class Files\Module 4\VIT Bhopal')