from setuptools import setup
setup(
    name='cli-anything-private',
    version='1.0.0',
    packages=['cli_anything.private'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-private=cli_anything.private:cli']},
)
