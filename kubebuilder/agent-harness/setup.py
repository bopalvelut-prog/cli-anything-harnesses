from setuptools import setup
setup(
    name='cli-anything-kubebuilder',
    version='1.0.0',
    packages=['cli_anything.kubebuilder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubebuilder=cli_anything.kubebuilder:cli']},
)
