from setuptools import setup
setup(
    name='cli-anything-slide',
    version='1.0.0',
    packages=['cli_anything.slide'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slide=cli_anything.slide:cli']},
)
