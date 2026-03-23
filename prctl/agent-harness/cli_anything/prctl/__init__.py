import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prctl running')
@cli.command()
def start(): click.echo('prctl started')
if __name__ == '__main__': cli()
