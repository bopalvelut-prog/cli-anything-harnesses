from setuptools import setup
setup(
    name='cli-anything-spec',
    version='1.0.0',
    packages=['cli_anything.spec'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spec=cli_anything.spec:cli']},
)
