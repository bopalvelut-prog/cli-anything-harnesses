import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bone running')
@cli.command()
def start(): click.echo('bone started')
if __name__ == '__main__': cli()
