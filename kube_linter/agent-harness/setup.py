from setuptools import setup
setup(
    name='cli-anything-kube_linter',
    version='1.0.0',
    packages=['cli_anything.kube_linter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kube_linter=cli_anything.kube_linter:cli']},
)
