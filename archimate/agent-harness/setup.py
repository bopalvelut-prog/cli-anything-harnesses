from setuptools import setup
setup(
    name='cli-anything-archimate',
    version='1.0.0',
    packages=['cli_anything.archimate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-archimate=cli_anything.archimate:cli']},
)
