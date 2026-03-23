import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mikmod running')
@cli.command()
def start(): click.echo('mikmod started')
if __name__ == '__main__': cli()
