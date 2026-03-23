import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('agent running')
@cli.command()
def start(): click.echo('agent started')
if __name__ == '__main__': cli()
