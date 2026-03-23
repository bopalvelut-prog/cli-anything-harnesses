from setuptools import setup
setup(
    name='cli-anything-dolt',
    version='1.0.0',
    packages=['cli_anything.dolt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dolt=cli_anything.dolt:cli']},
)
