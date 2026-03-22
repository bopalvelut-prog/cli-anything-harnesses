from setuptools import setup
setup(
    name='cli-anything-horizen',
    version='1.0.0',
    packages=['cli_anything.horizen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-horizen=cli_anything.horizen:cli']},
)
