from setuptools import setup
setup(
    name='cli-anything-couple',
    version='1.0.0',
    packages=['cli_anything.couple'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-couple=cli_anything.couple:cli']},
)
