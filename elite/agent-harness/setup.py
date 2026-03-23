from setuptools import setup
setup(
    name='cli-anything-elite',
    version='1.0.0',
    packages=['cli_anything.elite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elite=cli_anything.elite:cli']},
)
