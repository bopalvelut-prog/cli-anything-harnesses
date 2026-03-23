import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('teeth running')
@cli.command()
def start(): click.echo('teeth started')
if __name__ == '__main__': cli()
