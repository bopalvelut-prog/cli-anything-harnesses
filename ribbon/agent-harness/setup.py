from setuptools import setup
setup(
    name='cli-anything-ribbon',
    version='1.0.0',
    packages=['cli_anything.ribbon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ribbon=cli_anything.ribbon:cli']},
)
