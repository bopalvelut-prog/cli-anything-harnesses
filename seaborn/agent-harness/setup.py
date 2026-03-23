from setuptools import setup
setup(
    name='cli-anything-seaborn',
    version='1.0.0',
    packages=['cli_anything.seaborn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seaborn=cli_anything.seaborn:cli']},
)
