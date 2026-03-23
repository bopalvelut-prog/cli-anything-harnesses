from setuptools import setup
setup(
    name='cli-anything-kairos',
    version='1.0.0',
    packages=['cli_anything.kairos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kairos=cli_anything.kairos:cli']},
)
