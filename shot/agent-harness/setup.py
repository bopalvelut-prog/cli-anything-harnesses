from setuptools import setup
setup(
    name='cli-anything-shot',
    version='1.0.0',
    packages=['cli_anything.shot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shot=cli_anything.shot:cli']},
)
