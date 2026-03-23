from setuptools import setup
setup(
    name='cli-anything-planner',
    version='1.0.0',
    packages=['cli_anything.planner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-planner=cli_anything.planner:cli']},
)
