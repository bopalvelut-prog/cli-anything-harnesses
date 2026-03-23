import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('triple running')
@cli.command()
def start(): click.echo('triple started')
if __name__ == '__main__': cli()
