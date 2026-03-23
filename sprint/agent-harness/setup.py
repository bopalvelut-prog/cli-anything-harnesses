from setuptools import setup
setup(
    name='cli-anything-sprint',
    version='1.0.0',
    packages=['cli_anything.sprint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sprint=cli_anything.sprint:cli']},
)
