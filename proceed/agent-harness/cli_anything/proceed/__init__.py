import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('proceed running')
@cli.command()
def start(): click.echo('proceed started')
if __name__ == '__main__': cli()
