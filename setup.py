from setuptools import setup, find_packages

setup(
    name="serpentscribe",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    entry_points={
        'console_scripts': [
            'serpentscribe=src.cli:main',
        ],
    },
)
