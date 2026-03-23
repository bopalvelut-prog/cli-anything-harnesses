from setuptools import setup
setup(
    name='cli-anything-earn',
    version='1.0.0',
    packages=['cli_anything.earn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-earn=cli_anything.earn:cli']},
)
