import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('palace running')
@cli.command()
def start(): click.echo('palace started')
if __name__ == '__main__': cli()
