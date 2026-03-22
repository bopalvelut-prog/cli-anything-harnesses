import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('target')
def scan(target): subprocess.run(['trivy', 'image', target])
@cli.command()
def fs(): subprocess.run(['trivy', 'fs', '.'])
if __name__ == '__main__': cli()
