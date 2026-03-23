import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('javac running')
@cli.command()
def start(): click.echo('javac started')
if __name__ == '__main__': cli()
