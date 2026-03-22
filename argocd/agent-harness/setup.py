from setuptools import setup
setup(
    name='cli-anything-argocd',
    version='1.0.0',
    packages=['cli_anything.argocd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-argocd=cli_anything.argocd:cli']},
)
