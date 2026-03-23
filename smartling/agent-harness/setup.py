from setuptools import setup
setup(
    name='cli-anything-smartling',
    version='1.0.0',
    packages=['cli_anything.smartling'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smartling=cli_anything.smartling:cli']},
)
