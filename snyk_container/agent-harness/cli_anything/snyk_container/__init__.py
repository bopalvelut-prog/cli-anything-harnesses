import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('image')
def test(image): subprocess.run(['snyk', 'container', 'test', image])
@cli.command()
@click.argument('image')
def monitor(image): subprocess.run(['snyk', 'container', 'monitor', image])
if __name__ == '__main__': cli()
