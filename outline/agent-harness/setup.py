from setuptools import setup
setup(
    name='cli-anything-outline',
    version='1.0.0',
    packages=['cli_anything.outline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-outline=cli_anything.outline:cli']},
)
