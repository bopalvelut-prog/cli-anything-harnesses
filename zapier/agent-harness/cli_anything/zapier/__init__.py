import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Zapier zaps')
@cli.command()
def test(): click.echo('Zapier test')
if __name__ == '__main__': cli()
