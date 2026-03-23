import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blend running')
@cli.command()
def start(): click.echo('blend started')
if __name__ == '__main__': cli()
