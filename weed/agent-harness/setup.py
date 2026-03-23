from setuptools import setup
setup(
    name='cli-anything-weed',
    version='1.0.0',
    packages=['cli_anything.weed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weed=cli_anything.weed:cli']},
)
