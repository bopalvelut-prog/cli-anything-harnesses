from setuptools import setup
setup(
    name='cli-anything-increase',
    version='1.0.0',
    packages=['cli_anything.increase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-increase=cli_anything.increase:cli']},
)
