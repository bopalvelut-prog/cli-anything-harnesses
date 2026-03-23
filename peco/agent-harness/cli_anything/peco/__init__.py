import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('peco running')
@cli.command()
def start(): click.echo('peco started')
if __name__ == '__main__': cli()
