import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('motion running')
@cli.command()
def start(): click.echo('motion started')
if __name__ == '__main__': cli()
