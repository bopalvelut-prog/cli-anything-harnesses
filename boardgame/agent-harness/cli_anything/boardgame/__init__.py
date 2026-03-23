import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('boardgame running')
@cli.command()
def start(): click.echo('boardgame started')
if __name__ == '__main__': cli()
