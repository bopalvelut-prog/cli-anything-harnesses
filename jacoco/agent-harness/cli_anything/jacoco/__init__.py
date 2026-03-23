import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jacoco running')
@cli.command()
def start(): click.echo('jacoco started')
if __name__ == '__main__': cli()
