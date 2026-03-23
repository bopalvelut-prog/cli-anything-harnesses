import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Cursor start')
@cli.command()
def models(): click.echo('Cursor models')
if __name__ == '__main__': cli()
