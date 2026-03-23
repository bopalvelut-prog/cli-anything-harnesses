from setuptools import setup
setup(
    name='cli-anything-work',
    version='1.0.0',
    packages=['cli_anything.work'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-work=cli_anything.work:cli']},
)
