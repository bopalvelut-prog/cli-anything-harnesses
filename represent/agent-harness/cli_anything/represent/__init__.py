import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('represent running')
@cli.command()
def start(): click.echo('represent started')
if __name__ == '__main__': cli()
