import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gem running')
@cli.command()
def start(): click.echo('gem started')
if __name__ == '__main__': cli()
