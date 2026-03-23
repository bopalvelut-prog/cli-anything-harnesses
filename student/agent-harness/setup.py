from setuptools import setup
setup(
    name='cli-anything-student',
    version='1.0.0',
    packages=['cli_anything.student'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-student=cli_anything.student:cli']},
)
