import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('timeout running')
@cli.command()
def start(): click.echo('timeout started')
if __name__ == '__main__': cli()
