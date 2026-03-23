import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('colossus running')
@cli.command()
def start(): click.echo('colossus started')
if __name__ == '__main__': cli()
