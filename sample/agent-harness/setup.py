from setuptools import setup
setup(
    name='cli-anything-sample',
    version='1.0.0',
    packages=['cli_anything.sample'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sample=cli_anything.sample:cli']},
)
