#      pkg   .  pkg  . module
import alpha.mathlib.geometry as geometry
import sys

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module search path
# 1. current folder
# 2. folders in PYTHONPATH
#       Windows PATH1;PATH2;PATH3
#       Mac/Linux PATH1:PATH2:PATH3
# 3. default folders from installation

for path in sys.path:
    print(path)
