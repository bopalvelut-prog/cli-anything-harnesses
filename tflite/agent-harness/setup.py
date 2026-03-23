from setuptools import setup
setup(
    name='cli-anything-tflite',
    version='1.0.0',
    packages=['cli_anything.tflite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tflite=cli_anything.tflite:cli']},
)
