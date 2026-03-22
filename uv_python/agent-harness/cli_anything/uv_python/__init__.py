import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('project')
def init(project): subprocess.run(['uv', 'init', project])
@cli.command()
def sync(): subprocess.run(['uv', 'sync'])
@cli.command()
@click.argument('args', nargs=-1)
def run(args): subprocess.run(['uv', 'run'] + list(args))
if __name__ == '__main__': cli()
