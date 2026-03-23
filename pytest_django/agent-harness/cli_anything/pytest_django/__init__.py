import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pytest_django running')
@cli.command()
def start(): click.echo('pytest_django started')
if __name__ == '__main__': cli()
