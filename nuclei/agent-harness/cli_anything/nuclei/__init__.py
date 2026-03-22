import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('target')
def scan(target): subprocess.run(['nuclei', '-u', target])
@cli.command()
@click.argument('target')
def all(target): subprocess.run(['nuclei', '-u', target, '-as'])
if __name__ == '__main__': cli()
