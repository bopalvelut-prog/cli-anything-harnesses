import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crash running')
@cli.command()
def start(): click.echo('crash started')
if __name__ == '__main__': cli()
