from setuptools import setup
setup(
    name='cli-anything-ransack',
    version='1.0.0',
    packages=['cli_anything.ransack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ransack=cli_anything.ransack:cli']},
)
