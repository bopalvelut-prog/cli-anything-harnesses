import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('djinni running')
@cli.command()
def start(): click.echo('djinni started')
if __name__ == '__main__': cli()
