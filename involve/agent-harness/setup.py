from setuptools import setup
setup(
    name='cli-anything-involve',
    version='1.0.0',
    packages=['cli_anything.involve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-involve=cli_anything.involve:cli']},
)
