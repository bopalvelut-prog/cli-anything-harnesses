import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def client(): subprocess.run(['hysteria', '-c', 'config.yaml'])
@cli.command()
def server(): subprocess.run(['hysteria', 'server', '-c', 'config.yaml'])
if __name__ == '__main__': cli()
