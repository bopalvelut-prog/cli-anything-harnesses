from setuptools import setup
setup(
    name='cli-anything-mosh',
    version='1.0.0',
    packages=['cli_anything.mosh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mosh=cli_anything.mosh:cli']},
)
