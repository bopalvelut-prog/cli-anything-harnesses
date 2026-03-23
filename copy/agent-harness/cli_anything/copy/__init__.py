import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('copy running')
@cli.command()
def start(): click.echo('copy started')
if __name__ == '__main__': cli()
