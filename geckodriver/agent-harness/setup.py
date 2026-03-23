from setuptools import setup
setup(
    name='cli-anything-geckodriver',
    version='1.0.0',
    packages=['cli_anything.geckodriver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-geckodriver=cli_anything.geckodriver:cli']},
)
