from setuptools import setup
setup(
    name='cli-anything-solve',
    version='1.0.0',
    packages=['cli_anything.solve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-solve=cli_anything.solve:cli']},
)
