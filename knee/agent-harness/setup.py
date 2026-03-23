from setuptools import setup
setup(
    name='cli-anything-knee',
    version='1.0.0',
    packages=['cli_anything.knee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-knee=cli_anything.knee:cli']},
)
