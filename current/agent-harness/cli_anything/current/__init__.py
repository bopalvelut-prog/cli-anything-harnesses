import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('current running')
@cli.command()
def start(): click.echo('current started')
if __name__ == '__main__': cli()
