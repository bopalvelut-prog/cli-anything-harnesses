from setuptools import setup
setup(
    name='cli-anything-junior',
    version='1.0.0',
    packages=['cli_anything.junior'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-junior=cli_anything.junior:cli']},
)
