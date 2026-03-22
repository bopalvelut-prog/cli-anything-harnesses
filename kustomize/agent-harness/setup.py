from setuptools import setup
setup(
    name='cli-anything-kustomize',
    version='1.0.0',
    packages=['cli_anything.kustomize'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kustomize=cli_anything.kustomize:cli']},
)
