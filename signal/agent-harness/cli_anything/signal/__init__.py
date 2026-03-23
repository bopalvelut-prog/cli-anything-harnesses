import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('signal running')
@cli.command()
def start(): click.echo('signal started')
if __name__ == '__main__': cli()
