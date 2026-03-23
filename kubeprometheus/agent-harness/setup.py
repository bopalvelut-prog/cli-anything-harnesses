from setuptools import setup
setup(
    name='cli-anything-kubeprometheus',
    version='1.0.0',
    packages=['cli_anything.kubeprometheus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubeprometheus=cli_anything.kubeprometheus:cli']},
)
