import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bias running')
@cli.command()
def start(): click.echo('bias started')
if __name__ == '__main__': cli()
