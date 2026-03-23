import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('institute running')
@cli.command()
def start(): click.echo('institute started')
if __name__ == '__main__': cli()
