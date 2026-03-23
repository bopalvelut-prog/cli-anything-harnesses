import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('availability running')
@cli.command()
def start(): click.echo('availability started')
if __name__ == '__main__': cli()
