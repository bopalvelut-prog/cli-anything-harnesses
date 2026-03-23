import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rapid running')
@cli.command()
def start(): click.echo('rapid started')
if __name__ == '__main__': cli()
