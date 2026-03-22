from setuptools import setup
setup(
    name='cli-anything-kubewatch',
    version='1.0.0',
    packages=['cli_anything.kubewatch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubewatch=cli_anything.kubewatch:cli']},
)
