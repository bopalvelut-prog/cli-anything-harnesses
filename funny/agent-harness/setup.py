from setuptools import setup
setup(
    name='cli-anything-funny',
    version='1.0.0',
    packages=['cli_anything.funny'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-funny=cli_anything.funny:cli']},
)
