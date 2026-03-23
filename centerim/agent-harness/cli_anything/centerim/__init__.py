import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('centerim running')
@cli.command()
def start(): click.echo('centerim started')
if __name__ == '__main__': cli()
