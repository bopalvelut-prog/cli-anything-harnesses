from setuptools import setup
setup(
    name='cli-anything-click',
    version='1.0.0',
    packages=['cli_anything.click'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-click=cli_anything.click:cli']},
)
