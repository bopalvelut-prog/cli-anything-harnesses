from setuptools import setup
setup(
    name='cli-anything-visa',
    version='1.0.0',
    packages=['cli_anything.visa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-visa=cli_anything.visa:cli']},
)
