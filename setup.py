"""
Setup script for image-batch-processor package.
This file is maintained for backward compatibility.
The main configuration is in pyproject.toml.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="image-batch-processor",
    version="1.0.0",
    author="Carlos Rodriguez",
    author_email="carlos@example.com",
    description="A powerful CLI tool for batch processing images with various operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/image-batch-processor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
    install_requires=[
        "Pillow>=10.0.0",
        "click>=8.1.0",
        "PyYAML>=6.0",
        "rich>=13.0.0",
        "opencv-python>=4.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
            "pre-commit>=3.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "image-batch-processor=image_batch_processor.cli:main",
        ],
    },
    keywords="image batch processing cli resize convert",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/image-batch-processor/issues",
        "Source": "https://github.com/yourusername/image-batch-processor",
        "Documentation": "https://github.com/yourusername/image-batch-processor#readme",
    },
)