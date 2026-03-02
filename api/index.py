import os
import sys

# Add the root directory to sys.path so 'app' can be imported correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
