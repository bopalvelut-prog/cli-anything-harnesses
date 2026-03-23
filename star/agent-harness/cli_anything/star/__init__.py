import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('star running')
@cli.command()
def start(): click.echo('star started')
if __name__ == '__main__': cli()
