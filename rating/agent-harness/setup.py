from setuptools import setup
setup(
    name='cli-anything-rating',
    version='1.0.0',
    packages=['cli_anything.rating'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rating=cli_anything.rating:cli']},
)
