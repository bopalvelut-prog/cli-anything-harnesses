import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pine running')
@cli.command()
def start(): click.echo('pine started')
if __name__ == '__main__': cli()
