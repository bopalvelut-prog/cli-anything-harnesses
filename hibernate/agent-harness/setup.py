from setuptools import setup
setup(
    name='cli-anything-hibernate',
    version='1.0.0',
    packages=['cli_anything.hibernate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hibernate=cli_anything.hibernate:cli']},
)
