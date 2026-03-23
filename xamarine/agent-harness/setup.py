from setuptools import setup
setup(
    name='cli-anything-xamarine',
    version='1.0.0',
    packages=['cli_anything.xamarine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xamarine=cli_anything.xamarine:cli']},
)
