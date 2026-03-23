from setuptools import setup
setup(
    name='cli-anything-iris',
    version='1.0.0',
    packages=['cli_anything.iris'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-iris=cli_anything.iris:cli']},
)
