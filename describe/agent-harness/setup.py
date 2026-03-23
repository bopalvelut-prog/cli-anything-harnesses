from setuptools import setup
setup(
    name='cli-anything-describe',
    version='1.0.0',
    packages=['cli_anything.describe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-describe=cli_anything.describe:cli']},
)
