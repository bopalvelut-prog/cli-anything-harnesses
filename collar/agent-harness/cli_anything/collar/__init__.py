import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('collar running')
@cli.command()
def start(): click.echo('collar started')
if __name__ == '__main__': cli()
