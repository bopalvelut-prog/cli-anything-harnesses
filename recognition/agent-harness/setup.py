from setuptools import setup
setup(
    name='cli-anything-recognition',
    version='1.0.0',
    packages=['cli_anything.recognition'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recognition=cli_anything.recognition:cli']},
)
