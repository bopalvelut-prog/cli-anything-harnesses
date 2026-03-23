from setuptools import setup
setup(
    name='cli-anything-star',
    version='1.0.0',
    packages=['cli_anything.star'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-star=cli_anything.star:cli']},
)
