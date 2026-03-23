from setuptools import setup
setup(
    name='cli-anything-school',
    version='1.0.0',
    packages=['cli_anything.school'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-school=cli_anything.school:cli']},
)
