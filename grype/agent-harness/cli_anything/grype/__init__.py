import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('target')
def scan(target): subprocess.run(['grype', target])
@cli.command()
def dir(): subprocess.run(['grype', 'dir:.'])
if __name__ == '__main__': cli()
