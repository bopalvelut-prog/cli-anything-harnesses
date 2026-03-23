import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wealth running')
@cli.command()
def start(): click.echo('wealth started')
if __name__ == '__main__': cli()
