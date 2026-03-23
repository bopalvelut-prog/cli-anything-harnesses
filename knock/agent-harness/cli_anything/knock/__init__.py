import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('knock running')
@cli.command()
def start(): click.echo('knock started')
if __name__ == '__main__': cli()
