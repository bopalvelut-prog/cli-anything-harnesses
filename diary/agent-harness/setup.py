from setuptools import setup
setup(
    name='cli-anything-diary',
    version='1.0.0',
    packages=['cli_anything.diary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-diary=cli_anything.diary:cli']},
)
