from setuptools import setup
setup(
    name='cli-anything-amazon_rekognition',
    version='1.0.0',
    packages=['cli_anything.amazon_rekognition'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_rekognition=cli_anything.amazon_rekognition:cli']},
)
