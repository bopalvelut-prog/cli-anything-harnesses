import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tame running')
@cli.command()
def start(): click.echo('tame started')
if __name__ == '__main__': cli()
