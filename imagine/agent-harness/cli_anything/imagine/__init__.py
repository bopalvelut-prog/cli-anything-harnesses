import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('imagine running')
@cli.command()
def start(): click.echo('imagine started')
if __name__ == '__main__': cli()
