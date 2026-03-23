import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('suspect running')
@cli.command()
def start(): click.echo('suspect started')
if __name__ == '__main__': cli()
