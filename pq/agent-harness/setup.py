from setuptools import setup
setup(
    name='cli-anything-pq',
    version='1.0.0',
    packages=['cli_anything.pq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pq=cli_anything.pq:cli']},
)
