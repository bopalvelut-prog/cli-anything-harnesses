from setuptools import setup
setup(
    name='cli-anything-lesson',
    version='1.0.0',
    packages=['cli_anything.lesson'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lesson=cli_anything.lesson:cli']},
)
