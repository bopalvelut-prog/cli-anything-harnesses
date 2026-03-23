import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prospect running')
@cli.command()
def start(): click.echo('prospect started')
if __name__ == '__main__': cli()
