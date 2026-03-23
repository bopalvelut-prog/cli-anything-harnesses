import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('parking running')
@cli.command()
def start(): click.echo('parking started')
if __name__ == '__main__': cli()
