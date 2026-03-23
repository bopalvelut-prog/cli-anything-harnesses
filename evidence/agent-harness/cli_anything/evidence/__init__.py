import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('evidence running')
@cli.command()
def start(): click.echo('evidence started')
if __name__ == '__main__': cli()
