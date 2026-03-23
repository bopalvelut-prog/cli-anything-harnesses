from setuptools import setup
setup(
    name='cli-anything-tell',
    version='1.0.0',
    packages=['cli_anything.tell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tell=cli_anything.tell:cli']},
)
