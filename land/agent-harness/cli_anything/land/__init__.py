import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('land running')
@cli.command()
def start(): click.echo('land started')
if __name__ == '__main__': cli()
