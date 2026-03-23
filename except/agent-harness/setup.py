from setuptools import setup
setup(
    name='cli-anything-except',
    version='1.0.0',
    packages=['cli_anything.except'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-except=cli_anything.except:cli']},
)
