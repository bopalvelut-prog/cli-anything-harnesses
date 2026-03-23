import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('async running')
@cli.command()
def start(): click.echo('async started')
if __name__ == '__main__': cli()
