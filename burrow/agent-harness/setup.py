from setuptools import setup
setup(
    name='cli-anything-burrow',
    version='1.0.0',
    packages=['cli_anything.burrow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-burrow=cli_anything.burrow:cli']},
)
