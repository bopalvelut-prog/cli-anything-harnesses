from setuptools import setup
setup(
    name='cli-anything-must',
    version='1.0.0',
    packages=['cli_anything.must'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-must=cli_anything.must:cli']},
)
