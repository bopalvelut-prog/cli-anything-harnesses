from setuptools import setup
setup(
    name='cli-anything-chapter',
    version='1.0.0',
    packages=['cli_anything.chapter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chapter=cli_anything.chapter:cli']},
)
