from setuptools import setup
setup(
    name='cli-anything-smell',
    version='1.0.0',
    packages=['cli_anything.smell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smell=cli_anything.smell:cli']},
)
