from setuptools import setup
setup(
    name='cli-anything-kube_score',
    version='1.0.0',
    packages=['cli_anything.kube_score'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kube_score=cli_anything.kube_score:cli']},
)
