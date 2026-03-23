import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('native running')
@cli.command()
def start(): click.echo('native started')
if __name__ == '__main__': cli()
