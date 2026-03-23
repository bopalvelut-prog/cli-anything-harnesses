import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rescue running')
@cli.command()
def start(): click.echo('rescue started')
if __name__ == '__main__': cli()
