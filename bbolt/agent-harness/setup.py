from setuptools import setup
setup(
    name='cli-anything-bbolt',
    version='1.0.0',
    packages=['cli_anything.bbolt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bbolt=cli_anything.bbolt:cli']},
)
