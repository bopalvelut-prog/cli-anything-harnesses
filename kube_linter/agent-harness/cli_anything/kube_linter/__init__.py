import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def lint(): subprocess.run(['kube-linter', 'lint', '.'])
if __name__ == '__main__': cli()
