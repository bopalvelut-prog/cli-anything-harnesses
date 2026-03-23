from setuptools import setup
setup(
    name='cli-anything-soft',
    version='1.0.0',
    packages=['cli_anything.soft'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-soft=cli_anything.soft:cli']},
)
