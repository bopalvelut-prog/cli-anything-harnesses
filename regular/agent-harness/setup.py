from setuptools import setup
setup(
    name='cli-anything-regular',
    version='1.0.0',
    packages=['cli_anything.regular'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-regular=cli_anything.regular:cli']},
)
