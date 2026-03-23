import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('random running')
@cli.command()
def start(): click.echo('random started')
if __name__ == '__main__': cli()
