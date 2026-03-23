from setuptools import setup
setup(
    name='cli-anything-dollar',
    version='1.0.0',
    packages=['cli_anything.dollar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dollar=cli_anything.dollar:cli']},
)
