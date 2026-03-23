import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hang running')
@cli.command()
def start(): click.echo('hang started')
if __name__ == '__main__': cli()
