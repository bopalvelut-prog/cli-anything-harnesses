import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mechanism running')
@cli.command()
def start(): click.echo('mechanism started')
if __name__ == '__main__': cli()
