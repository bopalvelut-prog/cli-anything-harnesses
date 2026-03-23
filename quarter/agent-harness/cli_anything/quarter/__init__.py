import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quarter running')
@cli.command()
def start(): click.echo('quarter started')
if __name__ == '__main__': cli()
