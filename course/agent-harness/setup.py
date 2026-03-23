from setuptools import setup
setup(
    name='cli-anything-course',
    version='1.0.0',
    packages=['cli_anything.course'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-course=cli_anything.course:cli']},
)
