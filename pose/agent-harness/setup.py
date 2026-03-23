from setuptools import setup
setup(
    name='cli-anything-pose',
    version='1.0.0',
    packages=['cli_anything.pose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pose=cli_anything.pose:cli']},
)
