import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bunch running')
@cli.command()
def start(): click.echo('bunch started')
if __name__ == '__main__': cli()
