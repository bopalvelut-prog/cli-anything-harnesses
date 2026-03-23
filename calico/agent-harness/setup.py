from setuptools import setup
setup(
    name='cli-anything-calico',
    version='1.0.0',
    packages=['cli_anything.calico'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-calico=cli_anything.calico:cli']},
)
