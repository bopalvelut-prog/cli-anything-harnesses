from setuptools import setup
setup(
    name='cli-anything-teacher',
    version='1.0.0',
    packages=['cli_anything.teacher'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-teacher=cli_anything.teacher:cli']},
)
