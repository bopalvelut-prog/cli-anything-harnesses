from setuptools import setup
setup(
    name='cli-anything-ganglia',
    version='1.0.0',
    packages=['cli_anything.ganglia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ganglia=cli_anything.ganglia:cli']},
)
