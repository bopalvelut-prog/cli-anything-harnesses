import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('colonel running')
@cli.command()
def start(): click.echo('colonel started')
if __name__ == '__main__': cli()
