import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vertical running')
@cli.command()
def start(): click.echo('vertical started')
if __name__ == '__main__': cli()
