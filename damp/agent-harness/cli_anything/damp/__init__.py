import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('damp running')
@cli.command()
def start(): click.echo('damp started')
if __name__ == '__main__': cli()
