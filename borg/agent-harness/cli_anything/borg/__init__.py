import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('repo')
@click.argument('path')
def create(repo, path): subprocess.run(['borg', 'create', f'{repo}::{path}', path])
@cli.command()
@click.argument('repo')
def list(repo): subprocess.run(['borg', 'list', repo])
@cli.command()
@click.argument('repo')
def info(repo): subprocess.run(['borg', 'info', repo])
if __name__ == '__main__': cli()
