import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('beacon running')
@cli.command()
def start(): click.echo('beacon started')
if __name__ == '__main__': cli()
