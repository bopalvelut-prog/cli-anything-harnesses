import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('visual running')
@cli.command()
def start(): click.echo('visual started')
if __name__ == '__main__': cli()
