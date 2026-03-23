import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('paper running')
@cli.command()
def start(): click.echo('paper started')
if __name__ == '__main__': cli()
